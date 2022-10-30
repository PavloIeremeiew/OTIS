import math
def insor(a,x=0):
    x=a/(2*math.tan(math.degrees(180/5)))
    return(x)

def outsor(a,x=0):
    x=a/(2*math.sin(math.degrees(180/5)))
    return(x)