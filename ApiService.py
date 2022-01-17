# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 14:20:43 2022

@author: Bruno
"""

from sys import stderr
import requests
import pandas as pd
from datetime import date
import json
import os

today = date.today()
fecha = today.strftime("%Y-%d-%m")

class ApiService:
    def __init__(self):
        pass

    def run(self):
        print('Running ApiService', file=stderr)
        response = requests.get('https://jsonplaceholder.typicode.com/todos/')

        for i in range (1,201):
            with open(fecha+"-"+str(int(i))+".json", "w") as f:
                data = json.dump(response.json()[i-1], f)
            with open(fecha+"-"+str(int(i))+".json", "r") as f:  
                data = json.load(f)
                df = pd.DataFrame(data, index=[0])
                path = os.path.join("C:/Users/raich", "storage", fecha+"-"+str(int(i))+".csv")
                df.to_csv(path)
                
                
            