# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 02:01:24 2025

@author: numan
"""

def Bank_Atm():
    userWallet = 1000
    print("Kaplan bank'a hoş geldiniz.")
    while True:
        choices = input("Lütfen para yatırmak için (1) çekmek için (2) bakiye sorgusu için (3) çıkış için (0)' a basın: ")
        if choices == "1":
            addWallet = float(input("Yatırılacak tutar : "))
            if addWallet >= 0:
                userWallet += addWallet
                print(f"Bakiyeniz : {userWallet:.2f} ₺")
            else:
                print("Negatif sayı girişi yapılamaz.")
        elif choices == "2":
            withdraw = float(input("Çekilecek tutar : "))
            if withdraw <= userWallet:
                userWallet -= withdraw
                print(f"Bakiyeniz : {userWallet:.2f} ₺")
            else:
                print(f"Bakiyenden fazla para çekemezsin, mevcut bakiyen {userWallet:.2f} ₺")
        elif choices == "3":
            print(f"Bakiyeniz : {userWallet:.2f} ₺")
        elif choices == "0":
            break
        else:
            print("Yanlış tuşlama. Tekrar deneyin.")
        
    
Bank_Atm()