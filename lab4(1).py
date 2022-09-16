import math 
x=int(input("значення х"))
y=float((math.pow((x-4), 3) + math.log(x))/(abs(x+math.pow(math.tan(x),-1))) +math.pow(math.cos(x+2),3))
print(y)