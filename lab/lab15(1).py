from email import message
import tkinter as tk
import json
from tkinter import messagebox
from turtle import title 
T={}
with open('firms.json',encoding="utf-8") as f:
    templates = json.load(f)
T=templates
win=tk.Tk()
win['bg']='yellow'
win.geometry('450x280')
win.columnconfigure(0, minsize=450)
win.rowconfigure(1, minsize=150)
win.resizable(width=False,height=False)
Lmn = tk.Label(text="назва фірми",font=200,padx=10, pady=10)
entry = tk.Entry(foreground="white", background="grey", width=50)
def calcut():
    sss=entry.get()
    messagebox.showinfo(title="Кількість робіниківі", message=T[sss])

btn = tk.Button(text="Calculate", command=calcut,padx=10, pady=10)
Lmn.grid(row=0, column=0)
entry.grid(row=1, column=0)
btn.grid(row=2, column=0)
win.mainloop()