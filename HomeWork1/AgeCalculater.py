# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 17:02:02 2025

@author: numan
"""
def calculate_age():
    import datetime

    dayUser = int(input("Doğum gününüz (gün): "))
    monthUser = int(input("Doğum gününüz (ay): "))
    yearUser = int(input("Doğum yılınız: "))

    userBirthday = datetime.date(yearUser, monthUser, dayUser)
    today = datetime.date.today()
    age = today.year - userBirthday.year

    if userBirthday > today:
        print("Doğum tarihiniz şu anki tarihten büyük olamaz!!!")
    else:
        if (today.month, today.day) < (userBirthday.month, userBirthday.day):
            age -= 1
        print(f"Doğum tarihiniz: {userBirthday.strftime('%d.%m.%Y')}")
        print(f"Bugünün tarihi: {today.strftime('%d.%m.%Y')}")
        print(f"Yaşınız: {age}")

 

