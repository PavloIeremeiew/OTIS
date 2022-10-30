from asyncore import read
import json 
x= input("елемент:")
with open('element.json',encoding="utf-8") as f:
    templates = json.load(f)
print(templates[x])
x=input("буква(велика):")
for row in templates:
    if row[0]==x:
        print(row)