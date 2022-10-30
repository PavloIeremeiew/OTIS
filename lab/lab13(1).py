S = []


class ROCK:
    name = ""
    h = 0.0
    Cont = ""
    cant = ""

    def __init__(self, n, a, b, c):
        self.h = float(a)
        self.name = str(n)
        self.Cont = str(b)
        self.cant = str(c)

    def set_h(self, dd):
        self.h = float(dd)


N = int(input("кількість гір додати:"))
if N > 0:
    for i in range(0, N, 1):
        x = input("ім'я:")
        hh = int(input("висота:"))
        kk = input("континент:")
        cc = input("країна:")
        r = ROCK(x, hh, kk, cc)
        S.append(r)
    for i in range(0, N, 1):
        print(i + 1, S[i].name, " ", str(S[i].h), " ", S[i].Cont, " ", S[i].cant)

    S.sort(key=lambda o: o.name)
    print()
    
    for i in range(0, N, 1):
        print(i + 1, S[i].name, " ", str(S[i].h), " ", S[i].Cont, " ", S[i].cant)

l = int(input("кількість гір видалити:"))

if l > 0 and N > l:
    for i in range(0, l, 1):
        ll = int(input("номер:"))
        del S[ll - 1]
    for i in range(0, (N - l), 1):
        print(S[i].name, " ", str(S[i].h), " ", S[i].Cont, " ", S[i].cant)
