import random
from array import * 
masiv1=array('f',[])
N=int(input("степінь"))
x=float()
if N>=0:
 for i in range(0,N,1):
  x=3**i
  masiv1.append(x)
else:
    for i in range(N,0,1):
     x=3**i
     masiv1.append(x)
random.shuffle(masiv1)
print(masiv1)