# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 00:31:39 2025

@author: numan
"""
def restaurant_menu():
    menu = {
        "Çorbalar": {
            "Mercimek Çorbası": 85,
            "Kelle Paça": 120,
            "Brokoli Çorbası": 145,
            "Ezogelin": 100
        },
        "Ana Yemekler": {
            "Kebap": 180,
            "İskender": 220,
            "Tavuk Şiş": 150
        },
        "Tatlılar": {
            "Baklava": 120,
            "Künefe": 130,
            "Sütlaç": 90
        },
        "İçecekler": {
            "Coca Cola": 69,
            "Ayran": 35,
            "Su": 10,
            "Su (HAMİDİYE)": 4,
            "Şalgam (Acılı)": 45,
            "Şalgam (Acısız)": 40
        }
    }

    orders = []

    while True:
        choiceUser = input("\nÇorbalar (Ç), Ana Yemekler (A), Tatlılar (T), İçecekler (İ), Tüm Menü (M), Sipariş (S), Çıkış (Q): ")
        choiceUser = choiceUser.lower()
        
        if choiceUser == "q":
            print("Menüden çıkıldı.")
            break

        elif choiceUser == "m":
            for kategori, urunler in menu.items():
                print(f"\n--- {kategori} ---")
                for y, f in urunler.items():
                    print(f"{y}: {f} TL")

        elif choiceUser == "ç":
            print("\n--- Çorbalar ---")
            for y, f in menu["Çorbalar"].items():
                print(f"{y}: {f} TL")

        elif choiceUser == "a":
            print("\n--- Ana Yemekler ---")
            for y, f in menu["Ana Yemekler"].items():
                print(f"{y}: {f} TL")

        elif choiceUser == "t":
            print("\n--- Tatlılar ---")
            for y, f in menu["Tatlılar"].items():
                print(f"{y}: {f} TL")

        elif choiceUser == "i":
            print("\n--- İçecekler ---")
            for y, f in menu["İçecekler"].items():
                print(f"{y}: {f} TL")
        
        elif choiceUser == "s":
            product = input("Sipariş vermek istediğiniz ürünün ismini tam yazın: ")
            fond = False

            for kategori, urunler in menu.items():
                if product in urunler:
                    num = int(input("Kaç adet istiyorsunuz?: "))
                    price = urunler[product] * num
                    orders.append((product, num, price))
                    print(f"{num} adet {product} sepete eklendi. Ara toplam: {price} TL")
                    fond = True
                    break

            if not fond:
                print("Ürün menüde bulunamadı. Lütfen tam adını girin.")

    if orders:
        print("\n=== SİPARİŞ ÖZETİ ===")
        total = sum(price for _, _, price in orders)
        for product, num, price in orders:
            print(f"{num}x {product} - {price} TL")

        discount = 0
        if total >= 500:
            discount = total * 0.15
        elif total >= 300:
            discount = total * 0.10

        payable = total - discount
        print(f"\nToplam: {total} TL")
        if discount > 0:
            print(f"İndirim: -{discount:.2f} TL")
        print(f"Ödenecek Tutar: {payable:.2f} TL")
    
        payment = float(input("\nMüşteriden alınan para miktarını girin: "))
        while payment < payable:
            print("Yetersiz ödeme! Lütfen yeterli miktarı girin.")
            payment = float(input("Müşteriden alınan para miktarını girin: "))

        para_ustu = payment - payable
        print(f"Para Üstü: {para_ustu:.2f} TL")
        print("Teşekkürler! Afiyet olsun.")

    else:
        print("Hiçbir sipariş verilmedi.")

 



    
       
        