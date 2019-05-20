#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests as r
import shutil
from zipfile import ZipFile


# In[9]:


url = "http://ergast.com/downloads/f1db_csv.zip"


# In[10]:


file_name = url.split("/")[-1]

r = requests.get(url, stream=True)

with open(file_name, "wb") as f:
    shutil.copyfileobj(r.raw, f)


# In[11]:


with ZipFile(file_name,"r") as zip_ref:
    zip_ref.extractall("./data")


# In[ ]:




