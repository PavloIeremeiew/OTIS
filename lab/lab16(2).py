import pylab
import numpy as np
from bs4 import BeautifulSoup
import requests 
r=requests.get('https://prometheus.org.ua') 
x1=0
x2=0
x3=0
x4=0
if r.status_code==200:     
    wbs=BeautifulSoup(r.text,'html.parser')   
    namelist=wbs.find_all()     
    for name in namelist:     
     x1=x1+name.get_text().count('дистанційна')
     x2=x2+name.get_text().count('курси')
     x3=x3+name.get_text().count('програмування')
     x4=x4+name.get_text().count('Python')
       
x=np.array(["дистанційна","курси","програмування","Python"])
y=np.array([x1,x2,x3,x4])
pylab.bar (x, y)
pylab.show()