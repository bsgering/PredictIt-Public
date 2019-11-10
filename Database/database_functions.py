#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request as rq
import json as js
from dateutil import parser as pr
import datetime as dt
import pandas as pd


# In[2]:


predictitAPIall = 'https://www.predictit.org/api/marketdata/all/'


# In[3]:


def getdbmaterial():
    data = rq.urlopen(predictitAPIall)
    parsed_data = js.loads(data.read())
    return parsed_data


# In[36]:


def contractmakerfordb():
    date = dt.datetime.now()
    data = getdbmaterial()
    market = data['markets']
    contractlist = []
    for i in range (0, (len(market)-1)):
        current_market = market[i]
        market_name = market[i]['name']
        market_id = market[i]['id']
        contracts = current_market['contracts']
        for i in contracts:
            current_contract = i
            contract_id = current_contract['id']
            index = date.strftime("%Y%m%d'T'%H%M%S")+'-'+str(contract_id)
            contract_name = current_contract['name']
            contract_end_date = current_contract['dateEnd']
            contract_status = current_contract['status']
            contract_lasttradeprice = current_contract['lastTradePrice']
            contract_bestbuyyes = current_contract['bestBuyYesCost']
            contract_bestbuyno = current_contract['bestBuyNoCost']
            contract_bestsellyes = current_contract['bestSellYesCost']
            contract_bestsellno = current_contract['bestSellNoCost']
            contract_lastcloseprice = current_contract['lastClosePrice']
            contractlist_insert = [index, date, market_id, contract_id, market_name, contract_name, contract_end_date, 
                                   contract_status, contract_lasttradeprice, contract_bestbuyyes,
                                  contract_bestbuyno, contract_bestsellyes, contract_bestsellno,
                                  contract_lastcloseprice]
            contractlist.append(contractlist_insert)
    db_column_names = ['index','date', 'market_id', 'contract_id', 'market_name', 'contract_name', 'contract_end_date', 
                      'contract_status', 'contract_last_trade_price', 'contract_best_buy_yes_price',
                      'contract_best_buy_no_price', 'contract_best_sell_yes_price', 
                      'contract_best_sell_no_price', 'contract_last_close_price']
    database_df = pd.DataFrame(contractlist, columns = db_column_names)
    return database_df


# In[59]:


def pricecsvmaker(marketname1, marketname2, contractname1, contractname2):
    data = getdbmaterial()
    markets = data['markets']
    price_A = []
    price_B = []
    for i in range (0, (len(markets)-1)):
        current_market = market[i]
        market_name = market[i]['name']
        if market_name == marketname1:
            contracts = current_market['contracts']
            for i in contracts:
                current_contract = i
                contract_name = current_contract['name']
                if contract_name == contractname1:
                    price = current_contract['bestBuyYesCost']
                    price_A.append(price)
        if market_name == marketname2:
            contracts = current_market['contracts']
            for i in contracts:
                current_contract = i
                contract_name = current_contract['name']
                if contract_name == contractname2:
                    price = current_contract['bestBuyYesCost']
                    price_B.append(price)
    pricelist = price_A+price_B
    return pricelist

#test = pricecsvmaker('Which party will win the 2020 U.S. presidential election?', 
#                     'Will Mark Cuban run for president in 2020?',
#                    'Democratic', 'Will Mark Cuban run for president in 2020?'
#                    )
#with open('document.csv','a') as fd:
#    fd.write(myCsvRow)


# In[61]:


#test


# In[62]:





# In[15]:





# In[28]:





# In[ ]:




