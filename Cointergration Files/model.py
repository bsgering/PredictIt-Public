# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:06:50 2019

@author: Erik
"""

buyaggro = .1
sellaggro = .2
zscore = 1.96

for i in range(len(threemo)):
    x = threemo[i]/sixmo[i]
    
    if i > 90:
        mu = stat.mean(ratio)
        sigma = stat.stdev(ratio)
        if x > mu + (sigma*zscore):
            cash = cash + (round(tmohold*sellaggro)* threemo[i])
            tmohold -= round(tmohold*sellaggro)
            smohold += round((cash*buyaggro)/sixmo[i])
            cash = cash - ((round((cash*buyaggro)/sixmo[i]))* sixmo[i])
        if x < mu - (sigma*zscore):
            cash = cash + (round(smohold*sellaggro)* sixmo[i])
            tmohold -= round(smohold*sellaggro)
            smohold += round((cash*buyaggro)/threemo[i])
            cash = cash - ((round((cash*buyaggro)/threemo[i]))* threemo[i])
    
    portfolioVal = cash + (smohold*sixmo[i]) + (tmohold*threemo[i])
    value.append(portfolioVal)
    
    if i > 90:
        opt1.append((portfolioVal/value[90])*100)
        opt2.append((threemo[i]/threemo[90])*100)
    ratio.append(x)
    
print(coint(threemo, sixmo, autolag = 'aic'))

cash = cash + (tmohold * threemo[len(threemo)-1]) + (smohold * sixmo[len(sixmo)-1])
print('Pairs Return:' + str(cash/10000))
print("Regular Return:" + str(threemo[len(threemo)-1]/threemo[90]))

#plt.plot(opt1, color='green')
#plt.plot(opt2, color='red')
#plt.show()