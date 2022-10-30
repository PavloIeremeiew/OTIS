T=("zero","one","two","tree","four","five","six","seven","eight","nine")
S=input("numbers:")
s2=[]
t1=[]
for i in range(0,len(S),1):
     s2.append(int(S[i]))
for i in range(0,len(S),1):
    print(T[s2[i]])
print(T)