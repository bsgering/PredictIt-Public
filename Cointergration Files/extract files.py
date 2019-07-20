import csv
import pandas as pd
import statsmodels
import sqlite3

myFile = '2019-03-30.db'
#pd.read_excel("Data/testdata.xml")

conn = sqlite3.connect(myFile)
df = pd.read_sql("SELECT * FROM Prices WHERE contract_id = 67", conn)

df.to_csv('pricesprez.csv')

#contractid 67: Joe Biden US President
#contractid 27: Joe Biden Dem Nominee
#Note! The Dem Nom odds are weird and backwards for some reason