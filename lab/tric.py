import math

from numpy import False_
class TRIANGLE:
    a = 0.0
    b = 0.0
    c = 0.0
    s = 0.0
    t = True
    def __init__(self, x,y,z):
        self.a = float(x)
        self.b = float(y)
        self.c = float(z)
    def isset(self,x,y,z):
        if float(x+y)>z and float(x+z)>y and float(y+z)>x:
            print("існує")
            self.t = bool(True)
        else:
             print("не існує")
             self.t = bool(False)
    def CalcSquare(self, x,y,z,tt,p=0.0):
        p=(x+y+z)/2
        if tt==True:
         S=math.sqrt(p*(p-x)*(p-y)*(p-z))  
        else:
            S=0
        self.s = float(S)  
    def ShowSquare(self,S,tt):
        if tt==True:
         print("S:",str(S))    
    def ShowDim(self,x,y,z,tt):
        if tt==True:
         print("a:",str(x),"b:",str(y),"c:",str(z),"P:",str(x+y+z))  
