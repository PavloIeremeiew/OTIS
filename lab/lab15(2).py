from re import X
import tkinter as tk
win= tk.Tk()
x=0
x1=""
x2=""
x3=""
T=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
f=open('input.txt',"r",encoding="utf-8") 

z=f.read() 
for i in range(3):

 for j in range(3):
  fr = tk.Frame(master=win,relief=tk.RAISED,borderwidth=1)
  fr.grid(row=i, column=j)
  x=(i*3+j)*3
  x1=T[x] +':'+ str(z.count(T[x]))+'\n'
  x2=T[x+1] +':'+ str(z.count(T[x+1]))+'\n'
  if x<24:
   x3=T[x+2] +':'+ str(z.count(T[x+2]))+'\n'
  else:
    x3=""
  lab = tk.Label(master=fr, text=x1+x2+x3)
  lab.pack()

f.close() 
win.mainloop()