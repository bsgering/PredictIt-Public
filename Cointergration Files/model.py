# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:06:50 2019

@author: Erik
"""
from datetime import datetime

import statistics as stat
import pandas as pd
from statsmodels.tsa.stattools import coint
import matplotlib.pyplot as plt

def pairsTradeModel(sOne, sTwo, cash, buyaggro, sellaggro, zscore):
    ratio = []
    value = []
    opt1 = []
    opt2 = []
    sOneHold = 0
    sTwoHold = 0
        
    for i in range(len(sOne)):
        x = sOne[i]/sTwo[i]
        
        if i > 90:
            mu = stat.mean(ratio)
            sigma = stat.stdev(ratio)
            if x > mu + (sigma*zscore):
                cash = cash + (round(sOneHold*sellaggro)* sOne[i])
                sOneHold -= round(sOneHold*sellaggro)
                sTwoHold += round((cash*buyaggro)/sTwo[i])
                cash = cash - ((round((cash*buyaggro)/sTwo[i]))* sTwo[i])
            if x < mu - (sigma*zscore):
                cash = cash + round(sTwoHold*sellaggro)* sTwo[i]
                sTwoHold -= round(sTwoHold*sellaggro)
                sOneHold += round((cash*buyaggro)/sOne[i])
                cash = cash - ((round((cash*buyaggro)/sOne[i]))* sOne[i])
                               
        portfolioVal = cash + (sTwoHold * sTwo[i]) + (sOneHold * sOne[i])
        value.append(portfolioVal)
        
        if i > 90:
            opt1.append((portfolioVal/value[90])*100)
            opt2.append((sOne[i]/sOne[90])*100)
        ratio.append(x)
        
    print(coint(sOne, sTwo, autolag = 'aic'))
    
    cash = cash + (sOneHold * sOne[len(sOne)-1]) + (sTwoHold * sTwo[len(sTwo)-1])
    print('Pairs Return:' + str(cash/10000))
    print("Regular Return:" + str(sOne[len(sOne)-1]/sOne[90]))
        
    plt.plot(opt1, color='green')
    plt.plot(opt2, color='red')
    plt.show()
    
    return

def main():
    df = pd.read_csv(r'X:\Documents\PredictIt\pita\\stock.csv')   
    
    VOO = df['VOO'].tolist()
    SPY = df['SPY'].tolist()     
    
    pairsTradeModel(VOO, SPY, 10000, 0.10, 0.10, 0.53)
    return

if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print("Executed in:", datetime.now() - startTime)