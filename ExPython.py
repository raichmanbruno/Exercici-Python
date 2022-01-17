# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 09:29:59 2022

@author: Bruno
"""

import requests
import pandas as pd
from datetime import date
import json
import os

today = date.today()
fecha = today.strftime("%Y-%d-%m")

response = requests.get('https://jsonplaceholder.typicode.com/todos/')

for i in range (1,201):
    with open(fecha+"-"+str(int(i))+".json", "w") as f:
        data = json.dump(response.json()[i-1], f)
    df = pd.DataFrame(data, index=[0])
    path = os.path.join("C:/Users/raich", "storage", fecha+"-"+str(int(i))+".csv")
    df.to_csv(path)
