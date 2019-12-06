# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:25:10 2019

@author: Erik
"""

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
import numpy as np


# In[178]:


def pairsTradeModel(sOne, sTwo, cash, buyaggro, sellaggro, zscore, startday):
    startcash = cash
    ratio = sOne/sTwo
    sellonerat = (sOne-0.01)/sTwo
    selltworat = sOne/(sTwo-0.01)
    value = []
    opt1 = []
    opt2 = []
    sOneHold = 0
    sTwoHold = 0
    reserveAcct = 0
    sOnePur = 0
    sTwoPur = 0
    mu = stat.mean(ratio[0:startday-1])
    sigma = stat.stdev(ratio[0:startday-1])
    numtrades=0
    
    for i in range(len(sOne)):
        if cash > 850:
            reserveAcct += cash - 850
            cash -= cash - 850
        x = ratio[i]
        y1 = sellonerat[i]
        y2 = selltworat[i]
        if i > startday:
            # Changed the mean/st.dev algorithms to ones that only involved n calculations. Previously we performed
             # at least n^2 calculations, hence why it took forever...
            muold = mu
            mu = mu + ((ratio[i]-mu)/i)
            sigma = ((i-1-1)/(i-1))*(sigma**2)+(1/(i-1))*(ratio[i]-mu)*(ratio[i]-muold)
            # see https://stats.stackexchange.com/questions/24878/computation-of-new-standard-deviation-using-old-standard-deviation-after-change
            if x > mu + (sigma*zscore) and y1 > mu + (sigma*zscore):
                numtrades += 1
                cash = cash + (round(sOneHold*sellaggro)* (sOne[i]-0.01))
#                print("Sell " + str(sellaggro) + " Nomination")
                sOneHold -= round(sOneHold*sellaggro)
#                print("Buy " + str(buyaggro) + " Presidential")
                if sOneHold >0:
                    sOnePur -= round(sOneHold*sellaggro) * (sOnePur/sOneHold)
                else:
                    0
                
                if sTwoPur < 850:
                    sTwoHold += round((cash*buyaggro)/sTwo[i])
                    cash = cash - ((round((cash*buyaggro)/sTwo[i]))* sTwo[i])
                    sTwoPur += (round((cash*buyaggro)/sTwo[i]))* sTwo[i]
                    
            
            if x < mu - (sigma*zscore) and y2 < mu - (sigma*zscore):
                numtrades += 1
                cash = cash + round(sTwoHold*sellaggro)* (sTwo[i]-0.01)
#                print("Sell " + str(sellaggro) + " Presidential")
                sTwoHold -= round(sTwoHold*sellaggro)
#                print("Buy " + str(buyaggro) + " Nomination")
                if sTwoHold > 0:
                    sTwoPur -= round(sTwoHold*sellaggro) * (sTwoPur/sTwoHold)
                else:
                    0
                if sOnePur < 850:
                    sOneHold += round((cash*buyaggro)/sOne[i])
                    cash = cash - ((round((cash*buyaggro)/sOne[i]))* sOne[i])
                    sOnePur += (round((cash*buyaggro)/sOne[i]))* sOne[i]
                               
        portfolioVal = cash + (sTwoHold * sTwo[i]) + (sOneHold * sOne[i]) + reserveAcct
        value.append(portfolioVal)
        
        if i > startday:
            opt1.append((portfolioVal/value[startday])*100)
            opt2.append((sOne[i]/sOne[startday])*100)
        #ratio.append(x)
        
    #print(coint(sOne, sTwo, autolag = 'aic'))
    
    cash = cash + (sOneHold * sOne[len(sOne)-1]) + (sTwoHold * sTwo[len(sTwo)-1]) + reserveAcct
#    print('Pairs Return:' + str(cash/850))
#    print("Regular Return:" + str(sOne[len(sOne)-1]/sOne[90]))
        
    plt.plot(opt1, color='green')
    plt.plot(opt2, color='red')
    plt.show()
    
    print('-----------------------')
    print('zscore' + str(zscore))
    print('Final Value was ' + str(cash) + ' for a profit of ' + str(cash - startcash))
    print('You made ' + str(numtrades) + ' trades')
    print('You averaged $' + str((cash - startcash)/numtrades) + ' per trade')    
    return



def main():
    df = pd.read_csv('BidenAnalysis.csv')   
    #df = np.genfromtxt('stock.csv', dtype=float, delimiter=",",skip_header=1)
    #VOO = df[:,1]
    #SPY = df[:,2]
    numpy_df = np.asarray(df)
    #print(numpy_df)
    prez = numpy_df[:,1]
    #VOO.astype(int)
    nom = numpy_df[:,2]
    #SPY.astype(int)
    #VOO = df['VOO']
    #SPY = df['SPY']
    pairsTradeModel(nom, prez, 850, 0.30, 0.30, 1, 20000)
    return



if __name__ == "__main__":
    startTime = datetime.now()
    main()
    print("Executed in:", datetime.now() - startTime)


