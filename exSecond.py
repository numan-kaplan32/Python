# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 20:09:32 2025

@author: ARIBİLGİ
"""
import datetime
import math
import time


sqrtNum = math.sqrt(9)
print(type((sqrtNum)))

exNum = math.pow(2,4)
print(exNum)

facNum = math.factorial(10)
print(facNum)

pi = math.pi
print(pi)

r = float(input("yar çapını girin : "))
result = pi * math.pow(r,2) 
print("sonuç : " , round(result,2))

dateTime = datetime.datetime.now()
print(dateTime)

toDay = datetime.datetime.today()
timeDelta =datetime.timedelta(days=150, minutes= 40)#timedelta parametrelerle taih ekleme çıkarma işlemi yapar.
resultTime = toDay+timeDelta
print(resultTime)

strfTime = time.localtime()
print(time.strftime("%d.%m.%Y , %H.%M.%S"))

