from bs4 import BeautifulSoup
import requests 
H="H"
l=open('headers.txt',"w",encoding="utf-8") 
r=requests.get('https://w3schoolsua.github.io/html/html_headings.html') 
if r.status_code==200:     
    wbs=BeautifulSoup(r.text,'html.parser')   
    for i in range(1,7,1):
     H="h"+ str(i)
     namelist=wbs.find_all(H)     
     l.write("**********Заголовок "+H+'\n') 
     for name in namelist:         
        l.write(name.get_text()+'\n') 