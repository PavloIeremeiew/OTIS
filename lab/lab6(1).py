import math 
a=float(input("значення a"))
b=float(input("значення b"))
h=float(input("значення h"))
x=a
while x<=b:
  def f(x1):
   y=float(2**x1/math.fabs(x1**2+1)+ math.log2(math.fabs(math.fabs(x1)+1)))
   return(y)
  print(f(x))
  x=x+h
