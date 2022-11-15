from bs4 import BeautifulSoup, Tag
import requests 
l=open('holidays.txt',"w",encoding="utf-8") 
NN=input("Код країни (2 великі латинські букви):")
HH="https://date.nager.at/PublicHoliday/Country/"+NN
#HH="https://date.nager.at/PublicHoliday/Country/UA"
r=requests.get(HH) 
S=[]
S1=[]
if r.status_code==200:     
    wbs=BeautifulSoup(r.text,'html.parser')   
    #namelist=wbs.find_all('td.d-none.d-lg-table-cell')     
    namelist=wbs.find_all('a')
    for name in namelist:         
        S.append(name.get_text())
        #l.write(name.get_text()+'\n')
    for link in wbs.find_all("a"):         
        if 'href' in link.attrs: 
         if str(link).count("https:"):
          S1.append(link.attrs['href'])
         else:
            S1.append("https://date.nager.at"+link.attrs['href'])
          #l.write(link.attrs['href']+'\n')
    for i in range(len(S1)):
        l.write(S[i]+": "+S1[i]+'\n')