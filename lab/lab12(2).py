import random 
first=''
s="" 
T=[]
def sst(s=""):
    
   for j in range(0,7,1):
     first=random.randint(0,9)
     s=s+str(first)
   
   return(s)

n=int(input("N:"))
for i in range(0,n,1):
 a=sst()
 T.append("+38098"+a)
print(T)