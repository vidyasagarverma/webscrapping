#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Data-Science&where=india'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)


# In[2]:


results = soup.find(id='ResultsContainer')
print(results.prettify())


# In[3]:


job_elems = results.find_all('section', class_='card-content')
print(job_elems)


# In[4]:


for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




