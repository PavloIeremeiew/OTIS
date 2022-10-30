import pandas as pd
import csv  
import sys   
filename = "carcell.csv"  
df=pd.read_csv(filename, sep=';',encoding='cp1251')
df["m3"]=[int(input("toyota:")),int(input("shckoda:")),int(input("lamdorgini:")),int(input("nisan:"))]
df.to_csv("carcell1.csv", sep=';',encoding='cp1251')