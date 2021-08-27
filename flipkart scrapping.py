#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup 

import requests 

import csv

import pandas as pd


# In[2]:


url="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=7ec220e8-4f02-4150-9e0b-9e90cf692f4b&as-searchtext=laptop"

response = requests.get(url)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent,"html.parser")

print(soup.prettify)


# In[3]:


products=[]

prices=[]

ratings=[]

product=soup.find('div',attrs={'class':'_4rR01T'})

print(product.text)


# In[4]:


for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):

  name=a.find('div',attrs={'class':'_4rR01T'})

  price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})

  rating=a.find('div',attrs={'class':'_3LWZlK'})

  products.append(name.text)

  prices.append(price.text)

  ratings.append(rating.text)


# In[5]:


import pandas as pd

df = pd.DataFrame({'Product Name':products,'Prices':prices,'Ratings':ratings})

df.head()


# In[6]:


#webscrapping for mobile


# In[7]:


from bs4 import BeautifulSoup 

import requests 

import csv

import pandas as pd


# In[8]:


url="https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
response = requests.get(url)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent,"html.parser")

print(soup.prettify)


# In[15]:


products=[]

prices=[]

ratings=[]
product=soup.find('div',attrs={'class':'_4rR01T'})

print(product.text)


# In[12]:





# In[35]:


for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):

  name=a.find('div',attrs={'class':'_4rR01T'})

  price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})

  rating=a.find('div',attrs={'class':'_3LWZlK'})

  products.append(name.text)

  prices.append(price.text)

  ratings.append(rating.text)


# In[37]:


import pandas as pd

df1 = pd.DataFrame({'Product Name':products,'Prices':prices,'Ratings':ratings})

df1.head()


# In[18]:


url="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=7ec220e8-4f02-4150-9e0b-9e90cf692f4b&as-searchtext=laptop"

response = requests.get(url)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent,"html.parser")

print(soup.prettify)
response = requests.get(url)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent,"html.parser")

print(soup.prettify)


# In[19]:


products=[]

prices=[]

ratings=[]

product=soup.find('div',attrs={'class':'_4rR01T'})

print(product.text)


# In[32]:


for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):

  name=a.find('div',attrs={'class':'_4rR01T'})

  price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})

  rating=a.find('div',attrs={'class':'_3LWZlK'})

  products.append(name.text)

  prices.append(price.text)

  ratings.append(rating.text)


# In[ ]:





# In[33]:


print(df1.head)


# In[34]:


import pandas as pd

df = pd.DataFrame({'Product Name':products,'Prices':prices,'Ratings':ratings})

df.head()


# In[ ]:





# In[ ]:




