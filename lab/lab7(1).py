N= int(input("кількість рядків: "))
a=[]
a1=[]
for i in range(0,N,1):
 cc="рядок"+str(i+1)+":"
 s1=input(cc)
 a.append(s1)
 a1.append(len(s1))

x=int(max(a1))
s="*"
for i in range(0,N,1):
 l1=a[i]+s*(x-len(a[i]))
 print(l1)

