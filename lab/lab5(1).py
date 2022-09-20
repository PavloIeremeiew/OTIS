import math
x= float(input("значення х"))
if x>= 5.1:
   r= math.log2(3*x)- 7*math.sqrt(x)
elif x>= -0.7:
    r=math.e**x + 2*x**3
else:
    r=math.e**x + math.sin(x+ math.pi/4)

print(r)    