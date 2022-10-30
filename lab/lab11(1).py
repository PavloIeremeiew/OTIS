import csv  
import sys   
filename = "mydata.csv"    
T={}
T1={}
fd = open(filename, "r")     
reader = csv.reader(fd, delimiter=";")  
for row in reader: 
 T[row[0]]=row[1]
fd.close()
x=input("введіть Id:")
print(T[x])