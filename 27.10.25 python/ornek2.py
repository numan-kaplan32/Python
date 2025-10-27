# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 19:33:01 2025

@author: ARIBİLGİ
"""

import json


def addUser(name, surname):
    
    
    with open("Users.json", "r", encoding="utf-8") as file:
        data = json.load(file)


        new_id = len(data["Users"]) + 1
        new_user = {
            "id": new_id,
            "name": name,
            "surname": surname
        }

        data["Users"].append(new_user)
    with open("Users.json", "w", encoding="utf-8") as file:
         json.dump(data, file)


name = input("İsim: ")
surname = input("Soyisim: ")
addUser(name, surname)
