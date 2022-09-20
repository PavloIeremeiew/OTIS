import math 
a=int(input("значення a"))
b=int(input("значення b"))
h=int(input("значення h"))
sp=[]
for x in range(a,b+1,h):
  def f(x1):
   y=float(2**x1/math.fabs(x1**2+1)+ math.log2(math.fabs(math.fabs(x1)+1)))
   sp.append(y)
   
   return(y)
  print(f(x))  

print("найбільше значення ",min(sp))
print("найбільше значення ",max(sp))
