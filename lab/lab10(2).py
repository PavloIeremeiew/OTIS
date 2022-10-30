import shutil 
import os
s=[]
print(os.listdir (path=".") )
s=os.listdir (path=".")
os.mkdir ("D:\R_FILES", mode=0o777, dir_fd=None) 

for ind in s: 

 if ind[1]=='r':
   
    shutil.copy( ind, "D:\R_FILES")