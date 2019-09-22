#!/usr/bin/env python
# coding: utf-8

# In[164]:


import urllib.request as rq
import json as js
from dateutil import parser as pr
import datetime as dt
import pandas as pd


# In[165]:


predictitAPIall = 'https://www.predictit.org/api/marketdata/all/'


# In[18]:


def getdbmaterial():
    data = rq.urlopen(predictitAPIall)
    parsed_data = js.loads(data.read())
    return parsed_data


# In[19]:


#db = getdbmaterial()


# In[118]:


#market = db['markets']
#len(market)
#print(type(market))
#print(market[1].keys())
#print(market[1]['id'])
#contract = market[20]['contracts']
#print(contract[1].keys())
#print(len(contract))


# In[119]:


def marketlistmakerfordb():
    marketidlist = []
    for i in range (0, (len(market)-1)):
        market_id = market[i]['id']
        marketidlist.append(market_id)
    return marketidlist
        


# In[142]:


def contractmakerfordb():
    db = getdbmaterial()
    market = db['markets']
    date = dt.datetime.now()
    contractlist = []
    for i in range (0, (len(market)-1)):
        current_market = market[i]
        market_id = market[i]['id']
        contracts = current_market['contracts']
        for i in range(0, (len(contracts)-1)):
            current_contract = contracts[i]
            contract_id = current_contract['id']
            index = date.strftime("%Y%m%d'T'%H%M%S")+'-'+str(contract_id)
            contract_name = current_contract['longName']
            contract_end_date = current_contract['dateEnd']
            contract_status = current_contract['status']
            contract_lasttradeprice = current_contract['lastTradePrice']
            contract_bestbuyyes = current_contract['bestBuyYesCost']
            contract_bestbuyno = current_contract['bestBuyNoCost']
            contract_bestsellyes = current_contract['bestSellYesCost']
            contract_bestsellno = current_contract['bestSellNoCost']
            contract_lastcloseprice = current_contract['lastClosePrice']
            contractlist_insert = [index, date, market_id, contract_id, contract_name, contract_end_date, 
                                   contract_status, contract_lasttradeprice, contract_bestbuyyes,
                                  contract_bestbuyno, contract_bestsellyes, contract_bestsellno,
                                  contract_lastcloseprice]
            contractlist.append(contractlist_insert)
    db_column_names = ['Index','Date', 'Market ID', 'Contract ID', 'Contract Name', 'Contract End Date', 
                      'Contract Status', 'Contract Last Trade Price', 'Contract Best Buy Yes Price',
                      'Contract Best Buy No Price', 'Contract Best Sell Yes Price', 
                      'Contract Best Sell No Price', 'Contract Last Close Price']
    database_df = pd.DataFrame(contractlist, columns = db_column_names)
    return database_df


# In[162]:


#dataframe_insert = contractmakerfordb()
#engine = db.create_engine('sqlite:///predictit.sqlite3', echo=False)

#dataframe_insert.to_sql('Contracts', con=engine, if_exists='append', index_label='id')


# In[163]:


#engine.execute("SELECT COUNT(*) FROM Contracts").fetchall()


# In[ ]:




