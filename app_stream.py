import streamlit as st

def twitter(text):
    pass
    
def sitescrape(site):
    pass
    
def checkimage(img):
    pass
    
def gettext(f):
    pass
    
def whatsapp(a):
    pass
    
def emailid(a):
    pass
    
def audioi(a):
    pass
    
st.title('Data Extraction and Analysis')
st.write('Please enter Twitter-listening topic')
topic=st.text_input("label")
#call tweet function add topic as parameter
st.button('Listen', on_click=twitter, args=(topic,))

st.write('Please enter site to scrape')
site=st.text_input("label1")
#call webscrape function add site as parameter
st.button('Scrape', on_click=sitescrape, args=(site,))

st.write('Please enter select image file')
up=st.file_uploader('Upload image', type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None,  disabled=False)
#call image function add up as parameter
st.button('Detect_object', on_click=checkimage, args=(up,))

st.write('Please enter select PDF')
pdf=st.file_uploader('Upload PDF', type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
#call pdfreader function add pdf as parameter
st.button('Get_text', on_click=gettext, args=(pdf,))

st.write('Please enter select voice note file')
vn=st.file_uploader('Upload vn', type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None,  disabled=False)
#call audio function add vn as parameter
st.button('Transcribe')
st.button('Get_sentiment', on_click=audioi, args=(vn,))
st.title('Data Visualization')

#TO BE ADDED
st.title('Data Alerts')
st.write('Please enter whatsapp group ID ')
id=st.text_input("label2")

#call whatsapp function add id as parameter
st.button('Send Whatsapp Alert')
st.write('Please enter email address')
email=st.text_input("label3")

#call email function add email as parameter
st.button('Send email Alert')


def twitterscrape():
    st.write("Hi")
    