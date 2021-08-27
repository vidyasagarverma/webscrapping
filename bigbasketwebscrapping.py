#!/usr/bin/env python
# coding: utf-8

# In[3]:


import jovian


# In[1]:


from bs4 import BeautifulSoup as bs 
import requests


# In[2]:


eanCodeLists = [126906,40139631,40041188,40075201,40053874,1204742,40046735,40100963,40067874,40045943]


# In[3]:


urlopen = requests.get('https://www.bigbasket.com/pd/40053874').text


# In[4]:


soup = bs(urlopen,'html.parser')


# In[5]:


print(soup)


# In[6]:


ProductInfo = soup.find("h1", {"class": "GrE04"}).text  # .text will give us the text underlying that HTML element


# In[8]:


print(ProductInfo)


# In[10]:


ProductInfo.split(" ",1)


# In[14]:


ProductName=ProductInfo.split(" ",1)[1].split(',')[0]
print(ProductName)


# In[19]:


ProductDesc=soup.find("div",{"class":"_26MFu"}).text.strip().split("   ")[-1:]
print(ProductDesc)


# In[1]:


from bs4 import BeautifulSoup as bs 
import requests
eanCodeLists = [126906,40139631,40041188,40075201,40053874,1204742,40046735,40100963,40067874,40045943]
#define the product 
ProductNameList = []
ProductDescList = []

#For loop for iritate through EAN code list
for items in eanCodeLists:
    urlopen = requests.get('https://www.bigbasket.com/pd/'+str(items)).text
    soup = bs(urlopen,'lxml')
    ProductInfo = soup.find("h1", {"class": "GrE04"}).text.strip()
    ProductName=ProductInfo.split(" ",1)[1].split(',')[0]
    ProductNameList.append(ProductName)
    ProductDesc=soup.find("div",{"class":"_26MFu"}).text.strip().split("   ")[-1:]
    ProductDescList.append(ProductDesc)



 


# In[2]:


import pandas as pd
table_dict={"Product_Name":ProductNameList,"Product_desc":ProductDescList}
pd.DataFrame(table_dict)


# In[ ]:




