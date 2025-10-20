# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 10:13:07 2025

@author: numan
"""

term_count = 5
num1 = 1
num2 = 1
fibonacci = [num1, num2]

for i in range(2, term_count):
    next_num = num1 + num2
    fibonacci.append(next_num)
    num1, num2 = num2, next_num

for i in range(term_count):
    print(*fibonacci[:i+1])
