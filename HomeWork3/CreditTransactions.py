# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 09:27:41 2025

@author: numan
"""

def Credits():
    print("Hoş geldiniz.")
    while True:
        choices = input("Bir kredi çeşidi seçiniz: (İhtiyaç=1 Konut=2 Taşıt=3 çıkış=0): ")
        if choices == "0":
            print("Kredi işlemi sonlandırılıyor...")
            break
        try:
            amount = float(input("Çekmek istediğiniz kredi miktarını girin: "))
            month = int(input("Kredi ay sayısını girin: "))
            if amount <= 0 or month <= 0:
                print("Miktar ve ay sayısı pozitif olmalı.")
                continue
        except ValueError:
            print("Geçerli bir sayı girin.")
            continue

        if choices == "1":
            rate = 0.015
        elif choices == "2":
            rate = 0.012
        elif choices == "3":
            rate = 0.01
        else:
            print("Yanlış veya eksik tuşlama.")
            continue

        total_interest = amount * rate * month         
        total_pay = amount + total_interest              
        monthly_payment = total_pay / month             

        print(f"{month} ay sonunda ödenecek toplam faiz: {total_interest:.2f} ₺")
        print(f"Toplam geri ödeme: {total_pay:.2f} ₺")
        print(f"Aylık taksit: {monthly_payment:.2f} ₺")

Credits()
    