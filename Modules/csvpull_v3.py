#!/usr/bin/env python
# coding: utf-8

from datetime import datetime

import os, sqlite3
from glob import glob
import pandas as pd

def makecsv(candidateName, shortName):

    #creates the file list based on all files in the directory    
    dblocation = r'X:\Documents\PredictIt\pita\\'      
    os.chdir(dblocation)
    fileList = glob('*.{}'.format('db'))
    
    def pullMarkets(marketName, filelist):
        keyFrame = []
        keyList = []
        #Retrieves the marketID from the SQL file
        for i in range(len(filelist)):
            dbName = (filelist[i])
            conn = sqlite3.connect(dbName)
            df = pd.read_sql("SELECT market_id FROM Markets WHERE market_name = '%s' " %marketName, conn)
            keyFrame.append(df)
        #Turns the Dataframe into a list. There is probably a better way to do this so that it is never a dataframe, but I don't
        #know it at the moment and this works
        for i in range(len(keyFrame)):
            keyList.append(keyFrame[i].iat[0,0])
        return keyList
        
    #A sub function for the pullContract function, so that we can call "Pull Contract" as one function rather than a function and a loop.
    #Have to do this to index both lists at the same time and have the ids match with the right database.
    def subPullContract(marketID, contractName, filenum):
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
    
    def pullContract(marketIDs, contractName, filelist):
        contractIDs = []
        for i in range(len(filelist)):
            val = subPullContract(marketIDs[i], contractName, filelist[i])
            contractIDs.append(val)
        return contractIDs
    
    def pullFullDataFrame(filelist, conNums):
        priceDF = pd.DataFrame()
        for i in range(len(filelist)):
            dbName = (filelist[len(filelist) - i - 1 ])
            conNum = (conNums[len(filelist) - i - 1])
            conn = sqlite3.connect(dbName)
            df = pd.read_sql("SELECT buy_yes FROM Prices WHERE contract_id = '%d' " %conNum, conn)
            priceDF = df.append(priceDF, ignore_index = True)
           
            # Select from SQL command: Table: Prices
            #contractID: conNums[i]
            #value: buy_yes
            #send this to dataframe
            #append the info to a new dataframe
        return priceDF
    
    marketNumDem = pullMarkets('Who will win the 2020 Democratic presidential nomination?', fileList)    
    marketNumPrez = pullMarkets('Who will win the 2020 U.S. presidential election?', fileList)
        
    joeConNom = pullContract(marketNumDem, candidateName, fileList)
    joeConPrez = pullContract(marketNumPrez, candidateName, fileList)
    
    bidenPrezPrice = pullFullDataFrame(fileList, joeConPrez)
    bidenNominationPrice = pullFullDataFrame(fileList, joeConNom)
    
    mergedset = pd.merge(bidenPrezPrice, bidenNominationPrice, left_index=True, right_index = True, how = 'outer')
    
    mergedset.to_csv(r'X:\Documents\PredictIt\pita\%s.csv' % shortName)

    return

def main():
    makecsv('Andrew Yang', 'yang')
    return

if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print("Executed in:", datetime.now() - startTime)
