import math 
a=int(input("значення a"))
b=int(input("значення b"))
h=int(input("значення h"))
x=a
while x<=b:
  def f(x):
   y=float(2**x/math.fabs(x**2+1)+ math.log2(math.fabs(math.fabs(x)+1)))
   return(y)
  print(f(x))
  x=x+h
