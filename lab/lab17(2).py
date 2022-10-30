import pandas as pd
import numpy as np
import json
with open('squer.json',encoding="utf-8") as f:
    templates = json.load(f)
m1=pd.Series(templates)

for ll in m1:
 
 print((sum(m1)/3)-ll)