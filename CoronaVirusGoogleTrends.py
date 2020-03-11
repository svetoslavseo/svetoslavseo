#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pytrends
from pytrends.request import TrendReq
import pandas as pd
import time
import datetime
from datetime import datetime, date, time


# In[42]:


pytrends = TrendReq()
pytrends.build_payload(kw_list=['coronavirus',], timeframe='today 3-m', geo = 'GB', cat = 45)


# In[39]:


interest_over_time_df = pytrends.interest_over_time() 
print(interest_over_time_df.head())


# In[40]:


# Let's draw
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
dx = interest_over_time_df.plot.line(figsize = (40,8), title = "Coronavirus")
dx.set_xlabel('Date')
dx.set_ylabel('Trends Index')
dx.tick_params(axis='both', which='major', labelsize=18)

