#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[23]:


pd.set_option('display.max_columns', None)
churndata=pd.read_csv(r'G:\DSAICourse\python\Mca Project\dataset\Hz-CTU13_1.csv')#r is used to read as raw data
churndata


# In[24]:


churndata.shape


# In[25]:


churndata.describe()


# In[19]:


churndata.isnull().sum()


# In[22]:


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(20,20))
sns.heatmap(churndata.corr(),annot=True)


# In[ ]:




