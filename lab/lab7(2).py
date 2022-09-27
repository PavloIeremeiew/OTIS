import random 
N= int(input("кількість рядків: "))
ABC="ABCEHIKMOOOPTX" 
first=' '
x=0
s="" 
a=[]
for i in range(0,N,1):
  for j in range(0,N,1):
   first=random.choice(ABC) 
   s=s+first
  if s.count('O')>x:
   x=s.count('O')
   m=i
  a.append(s)
  print(s)
  s=""
print("найбільша кількість о: ",a[m])  