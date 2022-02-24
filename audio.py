# importing libraries
import speech_recognition as sri
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pathlib import Path
import pandas as pd
import librosa
import os
import statistics
import numpy as np
import time
# create a speech recognition object
r = sri.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition

def get_large_audio_transcription(path,cntr,directory):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_mp3(path)
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              min_silence_len=500,
                              # adjust this per requirement
                              silence_thresh=sound.dBFS-14,
                              # keep the silence for 1 second, adjustable as well
                              keep_silence=500,
                              )
    print("Estimated time in min:"+str(int((len(chunks)*3)/60)))
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(os.path.join(directory,folder_name+str(cntr))):
        os.mkdir(os.path.join(directory,folder_name+str(cntr)))
    whole_text = ""
    # process each chunk
    df=pd.DataFrame()
    if len(chunks)>0:
        d1=[]
        filz1=[]
        mfccs1=[]
        tx1=[]
        for i, audio_chunk in enumerate(chunks, start=1):
            # export audio chunk and save it in
            # the `folder_name` directory. 
            chunk_filename = os.path.join(os.path.join(directory,folder_name+str(cntr)), f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            # recognize the chunk
            d=[]
            filz=[]
            mfccs=[]
            tx=[]
            m=np.array([])
            with sri.AudioFile(chunk_filename) as source:
                audio_listened = r.record(source)
                # try converting it to text
                try:
                    text = r.recognize_google(audio_listened)
                    y, sr = librosa.core.load(chunk_filename)
                except sri.UnknownValueError as e:
                    text=("Error:"+ str(e))
                    duration=0
                    mfcc =np.array([])
                    mfccs.append(mfcc)
                else:
                    text = f"{text.capitalize()}. "
                    duration=librosa.get_duration(y=y, sr=sr)
                    mfcc = librosa.feature.mfcc(y=y, sr=44000, n_mfcc=5)
                    mfcc=mfcc.T
                    tx.append(text)
                    mfccs.append(mfcc)
                    d.append(duration)
                    filz.append(chunk_filename)
            print(mfccs)
            tx1.append(tx)
            np.append(m,mfccs)
            d1.append(d)
            filz1.append(filz)
        df=pd.DataFrame(filz1,columns=['namez'])
        df['textz']=tx1
        df['lengthz']=d1
        np.savetxt(str(cntr)+".csv", m, delimiter=",")
        
        dfz=pd.read_csv(str(cntr)+".csv",header=None)
        s=[dfz.iloc[[a],:].values for a in range(len(df)*10)]
        p=[i for i in s]
        if len(h)==len(df):
            df['mfccz']=p
    # return the text for all chunks detected
    return df


Dir = str(Path('b').parent.absolute())+"\\b"
directory = Path(Dir)
cntr=0
print(directory)
for fil in os.listdir(directory):
    cntr+=1
    tic=time.perf_counter()
    f=os.path.join(directory,fil)
    print("DF:"+f)
    print(f)
    path=f
    df=get_large_audio_transcription(path,cntr,directory)[0]
    p = os.path.join(directory, 'df_'+str(cntr)+'.csv')
    df.to_csv(p)
    print('df_'+str(cntr)+"saved")
    toc=time.perf_counter()
    print("Time taken:"+str((toc-tic)/60)+"min")
