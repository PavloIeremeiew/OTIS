
import numpy as np 
S=input("")
S2=input("")
L=[]
L2=[]
r1=""
r2=[]
L=S.split(' ')
L2=S2.split(' ')
A=[]
A2=[]
R1=[]

y=int(3)

if len(L)== len(L2):
    for i in range(0,len(L),1):
     A.append(int(L[i]))
     A2.append(int(L2[i]))

     R1.append(int(int(L2[i])+int(L[i])))
    M=np.array([A,A2],dtype=np.int32) 
    R=np.array(R1,dtype=np.int32) 
    print(M)
    
    for elen in (R):
        print(elen)
else:
    print("кількість чисел не рівна")