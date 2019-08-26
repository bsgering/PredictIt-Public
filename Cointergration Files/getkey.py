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

fileList = ['2019-03-30.db', '2019-04-02.db', '2019-04-09.db', '2019-04-16.db','2019-04-23.db',
            '2019-04-30.db','2019-05-07.db', '2019-05-14.db', '2019-05-21.db', '2019-05-28.db',
            '2019-06-04.db', '2019-06-11.db', '2019-06-18.db', '2019-06-25.db', '2019-07-02.db',
            '2019-07-09.db', '2019-07-16.db', '2019-07-23.db', '2019-07-30.db', '2019-08-06.db']


#Returns the MarketID for the specified querty
def pullMarkets(marketName):
    keyFrame = []
    keyList = []
    #Retrieves the marketID from the SQL file
    for i in range(len(fileList)):
        dbName = (fileList[i])
        conn = sqlite3.connect(dbName)
        df = pd.read_sql("SELECT market_id FROM Markets WHERE market_name = '%s' " %marketName, conn)
        keyFrame.append(df)
    #Turns the Dataframe into a list. There is probably a better way to do this so that it is never a dataframe, but I don't
    #know it at the moment and this works
    for i in range(len(keyFrame)):
        keyList.append(keyFrame[i].iat[0,0])
    return keyList

def pullContract(marketID, contractName, filenum):
    keyFrame = []
    #Retrieves the contractID from the SQL file
    dbName = (filenum)
    conn = sqlite3.connect(dbName)
    df = pd.read_sql("SELECT contract_id FROM Contracts WHERE market_id = '%d' AND contract_name = '%s' " % (marketID, contractName), conn)
    keyFrame.append(df)
    #Turns the Dataframe into a list. There is probably a better way to do this so that it is never a dataframe, but I don't
    #know it at the moment and this works
    conVal = (keyFrame[0].iat[0,0])
    return conVal

marketIDsDNom = pullMarkets('Who will win the 2020 Democratic presidential nomination?')
marketIDsPrez = pullMarkets('Who will win the 2020 U.S. presidential election?')

contractIDsDNom = []
contractIDsPrez = []

#I do this in a for loop rather than in the function because we have to match the market id to the same database.
#It can be done in the function probably, but I haven't figured out how yet
for i in range(len(fileList)):
     val = pullContract(marketIDsDNom[i], 'Joe Biden', fileList[i])
     contractIDsDNom.append(val)

for i in range(len(fileList)):
     val = pullContract(marketIDsPrez[i], 'Joe Biden', fileList[i])
     contractIDsPrez.append(val)

print(contractIDsDNom)
print(contractIDsPrez)

#Note! The Dem Nom odds are weird and backwards for some reason in one of the databases. It's the market where Joe Biden announces. 