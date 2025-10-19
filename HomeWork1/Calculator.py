# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 21:55:56 2025

@author: numan
"""

def simple_calculator():
    returnx = "r"

    while returnx.lower() == "r":    
        num1 = float(input("Birinci sayıyı girin: "))
        operator = input("Yapmak istediğiniz işlemi girin (+, -, *, /,%): ")
        num2 = float(input("İkinci sayıyı girin: "))

        if operator == "+":
            result = num1 + num2
            print("İşlem sonucunuz:", result)
        elif operator == "-":
            result = num1 - num2
            print("İşlem sonucunuz:", result)
        elif operator == "*":
            result = num1 * num2
            print("İşlem sonucunuz:", result)
        elif operator == "/":
            if num2 == 0:
                print("Hata! Bir sayı sıfıra bölünemez.")
            else:
                result = num1 / num2
                print("İşlem sonucunuz:", result)
        elif operator == "%":
            result = num1 * num2 /100
            print("İşlem sonucunuz:", result)
        else:
            print("Geçersiz işlem operatörü!")

        returnx = input("Yeni işlem için (r) tuşuna basın, çıkmak için herhangi bir tuş: ")

 

