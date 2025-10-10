# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 19:28:54 2025

@author: ARIBİLGİ
"""

import random


print("1 ile 50 arasında bir sayı tuttun. 3 hakkınız var!")

num = random.randint(1, 10)
claimUser = 0

while claimUser < 3:
    guessUser = int(input("Tahminini gir: "))

    if guessUser == num:
        print("Tebrikler! Doğru bildin!")
        break
    elif guessUser < num:
        print("Tahmin ettiğin sayı küçüktür.")
    else:
        print("Tahmin ettiğin sayı büyüktür.")

    claimUser += 1
    print(f"Kalan hakkın: {3 - claimUser}")

if claimUser == 3:
    print(f"Üzgünüm, bilemedin. Oyun bitti. Tutulan sayı: {num}")