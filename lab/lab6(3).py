import math 
def f(x1):
   y=float(2**x1/math.fabs(x1**2+1)+ math.log2(math.fabs(math.fabs(x1)+1)))
  
   
   return(y)
a=float(input("значення a"))
b=float(input("значення b"))
h=float(input("значення h"))
b1=int(round(b))
sp=[]
x=a
i=a
for i in range(b1+2):
  sp.append(f(x))
  print(f(x)) 
  x= x+h 
  if x> b:
    break

print("найменше значення ",min(sp))
print("найбільше значення ",max(sp))
print(sp)