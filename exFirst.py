# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 19:46:37 2025

@author: ARIBİLGİ
"""

for i in range(9):
   print(" " * (9 - i) , "*" * (2*i+1))
for j in range(1,9):
   print(" "*8+"*"*5)
   
import requests
istek = requests.get("https://www.google.com/?hl=tr")
print(istek.status_code)
if istek.status_code == 200:
    print("true")
else:
    print("false")
    
import random

num =(random.random())#1 ile 10 arası sayı yazar.
print(num)

intNum = random.randint(1, 10)
print(intNum)

rangeNum = random.randrange(1, 10, 2)#Kendine aralık belirleyip o aralıktan sayı seçer (star,stop,step).
print(rangeNum)

list1 = [5,23,234,565,844] 
randomV = random.choice(list1)#Liste içinden sayı seçer.
print(random)

random.shuffle(list1)#Listeyi karıştırır.
print(list1)

numGu = 0
falseGu = False 
while (falseGu == False):
    userNum = int(input("1 ile 10 arasında sayı seçiniz : (çıkmak için 0'a basın) "))
    numGu += 1
    if numGu == 3:
        print("yenildin")
        break 
        print(numGu + "Tahmin sayısı yaptınız") 
    elif userNum == 0:
        break
    elif userNum < intNum:
        print("Seçtiğiniz sayı küçüktür")  
        continue
    elif userNum > intNum:
        print("Seçtiğiniz sayı büyüktür")
        continue
    else:
        print("Seçtiğiniz sayı doğru")
    

