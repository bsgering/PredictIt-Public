# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from datetime import datetime

import pandas as pd
import matplotlib as plt
import statistics as stat

def pairsTradeModel(stockOne, stockTwo, ptarget, buyaggro, sellaggro):
    ratio = []
    portfolioValue = []
    benchmark = []
   
    cash = 100
    startValue = cash
    sOneHold = 0
    sTwoHold = 0
    
    for i in range(len(stockOne)):
        x = stockOne[i]/stockTwo[i]       
        if i > 10000:
            mu = stat.mean(ratio)
            sigma = stat.stdev(ratio)
            if x > (mu + (sigma * ptarget)):
                cash += (round(sOneHold*sellaggro) * stockOne[i])
                sOneHold -= round(sOneHold*sellaggro)
                sTwoHold += round((cash*buyaggro)/stockTwo[i])
                cash -= round((cash*buyaggro)/stockTwo[i]) * stockTwo[i]
            if x < (mu + (sigma * ptarget)):
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
    
    plt.pyplt.plot(benchmark, color="blue")
    plt.pyplt.plot(portfolioValue, color = "red")
    plt.pyplt.show()
    
    plt.pyplt.clf()
    plt.pyplt.plot(ratio)
    plt.pyplt.show()
    
    print("Total Benchmark Return:", benchmarkval[len(benchmark) -1]/benchmarkval[0])
    print("Total Pairs Return:", portfolioValue[len(benchmark) -1]/ portfolioValue[0])
    
    return


def main():
    df = pd.read_csv(r'X:\Documents\PredictIt\pita\\prices.csv')   
    
    nomination = df['buy_yes_y'].tolist()
    prez = df['buy_yes_x'].tolist()   
    
    pairsTradeModel(nomination, prez, 1.96,0.25,0.25)
    
    
    return

if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print("Test executed in:", datetime.now() - startTime)
#    exit()