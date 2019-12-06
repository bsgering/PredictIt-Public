#!/usr/bin/env python
# coding: utf-8

# In[7]:


from datetime import datetime
import statistics as stat
import pandas as pd
from statsmodels.tsa.stattools import coint
import matplotlib.pyplot as plt
import numpy as np
import discord as ds
from discord import Webhook, RequestsWebhookAdapter
import requests


# In[35]:





# In[178]:


def pairsTradeNotificationFunction(sOne, sTwo, buyaggro, sellaggro, zscore, stock1name, stock2name):
    ratio = sOne/sTwo
    ratioy1 = (sOne-0.01)/sTwo
    ratioy2 = sOne/(sTwo-0.01)
    value = []
    opt1 = []
    opt2 = []
    sOneHold = 0
    sTwoHold = 0
    reserveAcct = 0
    sOnePur = 0
    sTwoPur = 0
    mu = stat.mean(ratio)
    sigma = stat.stdev(ratio)
    muy1 = stat.mean(ratioy1)
    muy2 = stat.mean(ratioy2)
    sigmay1 = stat.stdev(ratioy1)
    sigmay2 = stat.stdev(ratioy2)
    buy = []
    sell = []
    finalposition = (len(ratio)-1)
    end = ratio[finalposition]
    y1 = ratioy1[finalposition]
    y2 = ratioy2[finalposition]
    message = []
    if end > mu+(sigma*zscore) and y1 > muy1 + (sigmay1*zscore):
        sell.append("Sell " + str(sellaggro*100) + "% of Stock: " + stock1name)
        buy.append("Use " + str(buyaggro*100) + "% of cash to purchase: " + stock2name)
        message.append(1)
    if end < mu - (sigma*zscore) and y2 < muy2 + (sigmay2*zscore):
        sell.append("Sell " +  str(sellaggro*100) + "% of Stock: " + stock2name)
        buy.append("Buy " + str(buyaggro*100) + "% of cash to purchase: " + stock1name)
        message.append(2)
    else:
        message.append(0)
        sell.append("Stop Buying/Selling " + stock1name)
        buy.append("Stop Buying/Selling " + stock2name)
    print(reserveAcct)
    
    return buy, sell, end, mu, sigma, message


# In[59]:


def notifyMe(csv, buyaggro, sellaggro, zscore, stock1name, stock2name, sendmessage):
    now = datetime.now()
    df = pd.read_csv(csv)   
    #df = np.genfromtxt('stock.csv', dtype=float, delimiter=",",skip_header=1)
    #VOO = df[:,1]
    #SPY = df[:,2]
    numpy_df = np.asarray(df)
    #print(numpy_df)
    Stock1 = numpy_df[:,1]
    #VOO.astype(int)
    Stock2 = numpy_df[:,2]
    #SPY.astype(int)
    #VOO = df['VOO']
    #SPY = df['SPY']
    messenger = []
    lists = pairsTradeNotificationFunction(Stock1, Stock2, buyaggro, sellaggro, zscore, stock1name, stock2name)
    messenger.append(lists[5])
    if len(lists[0]) == 0: 
        return 0
    if sendmessage[-1] == lists[5]
        return 1
    else:
        webhook = Webhook.partial(648325794665463809, 
                              'jVRuC2NIFqKlZPFQJkQSIOupd3H05qq3sV6Fu-pQoU_fmJKlJ9bRDHnAwaVoPe4uc5eR', 
                          adapter=RequestsWebhookAdapter())
        webhook.send('Time is ' + str(now.hour)+':'+str(now.minute)+', ' + str(lists[0]) +', ' + str(lists[1]))
        #webhook.send(lists[0])
        #webhook.send(lists[1])
    return messenger

#https://discordapp.com/api/webhooks/648325794665463809/jVRuC2NIFqKlZPFQJkQSIOupd3H05qq3sV6Fu-pQoU_fmJKlJ9bRDHnAwaVoPe4uc5eR
# In[60]:


#notifyMe('prices.csv', 0.3, 0.3, 1, 'Stock1', 'Stock2')


# In[ ]:


#https://discordapp.com/api/webhooks/643245527994990592/lq2y-B1sVr7sUcz-TWtiv0QVqoAex5BgEFd9YcBtVqfCS2qpzcip7E-zpds7-ZjkPtLr

