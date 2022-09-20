import math 
x=int(input("значення х"))
def f(x):
 y=float(math.fabs(math.sin(2*x)+math.cos(3*x+1)+ math.tan(math.fabs(x)+0.7))+ math.log10(math.fabs(x-4)))
 return(y)

print(f(x))