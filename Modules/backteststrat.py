#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import statistics as st
from scipy.stats import norm


# In[ ]:





# In[5]:


def backteststrat (tolerance, ratiodataset):        
    data = []
    for i in len(ratiodataset):
        if i < 2:
            print('statserror')
        else:
            ratiotest = ratiodataset.iloc[i,3]
            backratios = ratiodataset.iloc[:i-1,3]
            stdevcomparevalue = st.stdev(backratios)
            averageratio = st.mean(backratios)
            Ztolerance = norm.ppf(tolerance)
            withintolerance = Ztolerance*stdevcomparevalue
            if ratiotest > (averageratio+withintolerance):
                data.append([ratiodataset.iloc[i,0], ratiodataset.iloc[i,3], 1])
            elif ratiotest < (averageratio-withintolerance):
                data.append([ratiodataset.iloc[i,0], ratiodataset.iloc[i,3], 1])
            else:
                data.append([ratiodataset.iloc[i,0], ratiodataset.iloc[i,3], 0])                
    col_names =  ['Timestamp', 'Ratio', 'Trade?']
    backtest_trade_df = pd.DataFrame(data, columns = col_names)
    return backtest_trade_df


# In[ ]:




