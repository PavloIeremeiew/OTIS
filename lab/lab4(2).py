import math 
x=int(input("значення х"))
y=int(input("значення y"))
z=int(input("значення z"))
r=float(12*(math.pow(x,2)+ math.sin(y))+ math.sqrt(math.pow(z, 2)+1)/math.log(abs(abs(z)+0.07),3))
print(r)