# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from datetime import datetime

import pandas as pd
#import matplotlib.pyplt as plt
import statistics as stat

def pairsTradeModel(stockOne, stockTwo, zscore, buyaggro, sellaggro):
    ratio = []
    portfolioValue = []
    benchmark = []
   
    cash = 10000
    startValue = cash

    sOneHold = 0
    sTwoHold = 0
    

    for i in range(len(stockOne)):
    
        x = stockOne[i]/stockTwo[i]

        if i > 90:
            mu = stat.mean(ratio)
            sigma = stat.stdev(ratio)
            if x > (mu + (sigma * zscore)):
                cash += (round(sOneHold*sellaggro)* stockOne[i])
                sOneHold -= round(sOneHold*sellaggro)
                sTwoHold += round((cash*buyaggro)/stockTwo[i])
                cash = cash - ((round(sTwoHold*buyaggro)/stockTwo[i])) * stockTwo[i]
            if x < (mu - (sigma * zscore)):
                cash += (round(sTwoHold*sellaggro) * stockOne[i])
                sTwoHold -= round(sTwoHold*sellaggro)
                sOneHold += round((cash*buyaggro)/stockTwo[i])
                cash -= round((cash*buyaggro)/stockOne[i]) * stockOne[i]  
        ratio.append(x)        
        value = cash + (sOneHold * stockOne[i]) + (sTwoHold * stockTwo[i])
        value = (value/startValue) * 100
        benchmarkval = (stockOne[i]/stockOne[0]) * 100
        portfolioValue.append(value)
        benchmark.append(benchmarkval)
    
#    plt.plot(benchmark, color="blue")
#    plt.plot(portfolioValue, color = "red")
#    plt.show()
#    
#    plt.clf()
#    plt.plot(ratio)
#    plt.show()
#    
    print("Total Benchmark Return:", benchmark[len(benchmark)-1]/benchmark[0])
    print("Total Pairs Return:", portfolioValue[len(portfolioValue)-1]/ portfolioValue[0])
    print(portfolioValue[len(portfolioValue)-1])
    
    return


def main():
    df = pd.read_csv(r'X:\Documents\PredictIt\pita\\stock.csv')   
    
    nomination = df['VOO'].tolist()
    prez = df['SPY'].tolist()   
    
    pairsTradeModel(nomination, prez, 1.96,0.1,0.2)
    
    
    return

if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print("Executed in:", datetime.now() - startTime)
#    exit()