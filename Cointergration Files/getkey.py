# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 12:14:31 2019

@author: Erik
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 09:40:33 2019

@author: Erik
"""

#TO DO:
#Convert Lookup to a function:

import csv
import pandas as pd
import statsmodels
import sqlite3

keyListDNom = []
keyListPrez = []


fileList = ['2019-03-30.db', '2019-04-02.db', '2019-04-09.db', '2019-04-16.db','2019-04-23.db',
            '2019-04-30.db','2019-05-07.db', '2019-05-14.db', '2019-05-21.db', '2019-05-28.db',
            '2019-06-04.db', '2019-06-11.db', '2019-06-18.db', '2019-06-25.db', '2019-07-02.db',
            '2019-07-09.db', '2019-07-16.db', '2019-07-23.db', '2019-07-30.db', '2019-08-06.db']


#Gets the Market ID for The Democratic Nomination Market
for i in range(len(fileList)):
    dbName = (fileList[i])
    conn = sqlite3.connect(dbName)
    df = pd.read_sql("SELECT market_id FROM Markets WHERE market_name = 'Who will win the 2020 Democratic presidential nomination?' ", conn)
    keyListDNom.append(df)

#Gets the Market ID for The Presidential Election
for i in range(len(fileList)):
    dbName = (fileList[i])
    conn = sqlite3.connect(dbName)
    df2 = pd.read_sql("SELECT market_id FROM Markets WHERE market_name = 'Who will win the 2020 U.S. presidential election?' ", conn)
    keyListPrez.append(df2)
    
#df.values.tolist()

print(keyListDNom)
print(keyListPrez)


#contractid 67: Joe Biden US President
#contractid 27: Joe Biden Dem Nominee
#Note! The Dem Nom odds are weird and backwards for some reason
