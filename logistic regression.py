#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[11]:


pd.set_option('display.max_columns', None)
churndata=pd.read_csv('G:\DSAICourse\python\Mca Project\dataset\Hz-CTU13_1.csv')#r is used to read as raw data
churndata


# In[12]:


churndata.shape


# In[13]:


churndata.describe()

