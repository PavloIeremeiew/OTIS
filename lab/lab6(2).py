import math 
a=int(input("значення a"))
b=int(input("значення b"))
h=int(input("значення h"))

for x in range(a,b+1,h):
  def f(x1):
   y=float(2**x1/math.fabs(x1**2+1)+ math.log2(math.fabs(math.fabs(x1)+1)))
   return(y)
  print(f(x))
 