# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 10:19:36 2019

@author: Erik
"""

from statsmodels.tsa.stattools import coint
import csv

def openfiles (x):
    with open(x, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    return your_list

P = openfiles('pricesnom.csv')
Q = openfiles('pricesprez.csv')

print (P)
#coint(P,Q)

#I think this will work once the list of lists is converted to integers
#but not %100 sure

