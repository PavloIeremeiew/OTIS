from bs4 import BeautifulSoup, Tag
import requests 
l=open('holidays.txt',"w",encoding="utf-8") 
NN=input("Код країни (2 великі латинські букви):")
HH="https://date.nager.at/PublicHoliday/Country/"+NN
#HH="https://date.nager.at/PublicHoliday/Country/UA"
r=requests.get(HH) 

if r.status_code==200:     
    wbs=BeautifulSoup(r.text,'html.parser')   
    #namelist=wbs.find_all('td.d-none.d-lg-table-cell')     
    namelist=wbs.find_all('td')
    for name in namelist:         
        #print(name.get_text()+'\n') 
        l.write(name.get_text()+'\n')