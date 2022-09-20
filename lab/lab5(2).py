import math
a= float(input("стороно квадрата"))
if a<0:
    print("так не бува")
else:
  x= float(input("кордината x точки"))
  y= float(input("кордината y точки"))
  if (abs(a)/2)>= (abs(x)) and (abs(a)/2) >= (abs(y)):
      print("точка в квадраті")
  else:
     print("точка поза квадратом")
