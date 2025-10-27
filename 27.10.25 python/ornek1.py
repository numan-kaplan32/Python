# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 19:16:58 2025

@author: ARIBİLGİ
"""

import json

data = {"name": "Numan","surname":"Kaplan"}
dataJson = json.dumps(data)

print(dataJson)


dataJson = '{"name": "Numan","surname":"Kaplan"}'
data = json.loads(dataJson)

print(data)

#Json'a veri yazma

data = {"name": "Numan","surname":"Kaplan"}

with open("data.json","w") as file:
    json.dump(data, file)

with open("data.json","r") as file:
    data = json.load(file)
    print(data)