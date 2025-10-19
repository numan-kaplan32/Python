# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 16:01:46 2025

@author: numan
"""
from RestaurantMenu import restaurant_menu
from Calculator import simple_calculator
from AgeCalculater import calculate_age

while True:
    print("\nHangi programı çalıştırmak istersiniz?")
    print("1 - Restaurant Menüsü")
    print("2 - Hesap Makinesi")
    print("3 - Yaş Hesaplayıcı")
    print("Q - Çıkış")

    choice = input("Seçiminizi girin (1/2/3/Q): ")

    if choice == "1":
        restaurant_menu()
    elif choice == "2":
        simple_calculator()
    elif choice == "3":
        calculate_age()
    elif choice.lower() == "q":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen 1, 2, 3 veya Q girin.")


