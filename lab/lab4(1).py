import math 
x1=int(input("значення х"))
def f(x):
 y=float((math.pow((x-4), 3) + math.log(x))/(abs(x+math.pow(math.tan(x),-1))) +math.pow(math.cos(x+2),3))
 return(y)

print(f(x1))