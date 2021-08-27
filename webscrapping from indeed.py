#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

URL = 'https://au.indeed.com/jobs?q=data+science+internship&l=Sydney+NSW'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')


# In[2]:


results = soup.find(id='resultsCol')

print(results.prettify())


# In[3]:


job_elems = results.find_all('div', class_='jobsearch-SerpJobCard')
print(job_elems)


# In[4]:


for job_elem in job_elems:
    print(job_elem, end='\n'*2)


# In[5]:


for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='sjcl')
    location_elem = job_elem.find('div', class_='summary')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
print()


# In[ ]:





# In[ ]:




