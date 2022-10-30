import random 
first=''
s="" 
def sst(N,M,a,s=""):
    for i in range(0,N,1):
        for j in range(0,M,1):
            first=random.choice(a) 
            s=s+first
        print(s)
        s=""

n=int(input("N:"))
m=int(input("M:"))
sst(n,m,"abcdefghijklmnopqrstuvwxyz")
