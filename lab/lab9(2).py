T=set() 
for i in range(101,250,1):
     if i%3==0:
        T.add(i)
print(T)
for i in range(101,250,1):
     if i%6==0:
        T.discard(i)
print(T)