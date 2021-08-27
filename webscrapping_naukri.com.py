#!/usr/bin/env python
# coding: utf-8

# In[1]:



from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests


# In[2]:


df = pd.DataFrame(columns=['Title','Company','URL'])


# In[3]:


url='https://www.naukri.com/government-jobs'


# In[4]:


page=requests.get(url)


# In[5]:


page.text


# In[6]:


driver=webdriver.Chrome("C:\\Users\\Vidya sagar\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get(url)
time.sleep(3)
soup=BeautifulSoup(driver.page_source,'html5lib')
print(soup.prettify())


# In[7]:


driver.close()


# In[8]:


df = pd.DataFrame(columns=['Title','Company','URL'])


# In[9]:


results=soup.find(class_='list')


# In[10]:


results


# In[11]:


job_elems=results.find_all('article',class_="jobTuple bgWhite br4 mb-8")
job_elems


# In[13]:


for job_elem in job_elems:
    URL = job_elem.find('a',class_='title fw500 ellipsis').get('href')
    print(URL)
    #post title
    Title=job_elem.find('a',class_='title fw500 ellipsis')
    print(Title.text)
     # Company Name
    Company = job_elem.find('a',class_='subTitle ellipsis fleft')
    print(Company)

    print(" "*2)
    df=df.append({'URL':URL,'Title':Title.text,'Company':Company.text},ignore_index = True)


# In[14]:


df.head(20)


# In[ ]:




