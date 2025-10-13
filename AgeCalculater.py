# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 17:02:02 2025

@author: numan
"""
import datetime

dayUser = int(input("Doğum gününüz (gün): "))
monthUser = int(input("Doğum gününüz (ay): "))
yearUser = int(input("Doğum gününüz (yıl): "))

userBirthday = datetime.date(yearUser, monthUser, dayUser)
today = datetime.date.today()
age = today.year - userBirthday.year
if (today.month, today.day) < (userBirthday.month, userBirthday.day):
    print("Doğum tarihiniz şuanki tarihten büyük olamaz!!!")
    
else:
    print(f"Doğum tarihiniz: {userBirthday.strftime('%d.%m.%Y')}")
    print(f"Bugünün tarihi: {today.strftime('%d.%m.%Y')}")
    print(f"Yaşınız: {age}")
