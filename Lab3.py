import sys

a = input("число: ")

if len(a) != 3:
    print("Число не 3х значне")
    sys.exit()

for i in a:
    print(i)