import random
def sst(N,M,a,s=""):
    first=''
    s="" 
    l=[]
    for i in range(0,N,1):
        for j in range(0,M,1):
            first=random.choice(a) 
            s=s+first
        l.append(s)
        s=""
    return(l)