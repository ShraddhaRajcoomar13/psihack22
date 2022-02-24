#!/usr/bin/env python
# coding: utf-8

# In[3]:


from lxml import html
import requests

page = requests.get('https://www.education.gov.za/Programmes/EMIS/EMISDownloads.aspx')
webpage = html.fromstring(page.content)

t=[i for i in webpage.xpath('//a/@href') if "LinkClick.aspx?fileticket=" in i]


# In[13]:


for i in range(len(t)):
    url=('https://www.education.gov.za/'+str(t[i]))
    print(url)
    r = requests.get(url, allow_redirects=True)
    open('do/new'+str(i)+'.xlsx', 'wb').write(r.content)


# In[ ]:


import pandas as pd
df=pd.DataFrame()
for i in range(len(t)):
    df.append(pd.read_excel('do/new'+str(i)+'.xlsx')).drop_duplicates().to_excel('masterschools.xlsx')


# In[14]:


print(len(t))


# In[ ]:




