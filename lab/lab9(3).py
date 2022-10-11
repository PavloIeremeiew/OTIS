s=("Водень","Гелій","Літій","Берилій","Бор","Вуглець","Азот","Кисень","Фтор","Неон")
S1=("H","He","Li","Be","B","C","N","O","F","Ne")
T={}
N=int(input("скільки елементів(до 10):"))
for i in range(0,N,1):
 x=int(input("число елемента(до 10):"))
 T[S1[x-1]]=s[x-1]

for i in sorted(T.items(), key=lambda para: para[1]):
    print(i)