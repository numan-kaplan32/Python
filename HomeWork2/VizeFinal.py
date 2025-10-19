# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 15:38:27 2025

@author: numan
"""

def fightin_calculate_grade():

    midterm1 = float(input("1. vize notunu gir: "))
    midterm2 = float(input("2. vize notunu gir: "))
    final_exam = float(input("Final notunu gir: "))

    midterm_average = (midterm1 + midterm2) / 2
    total_average = (midterm_average * 0.3) + (final_exam * 0.7)

    print(f"\nVize Ortalaması: {midterm_average:.2f}")
    print(f"Genel Ortalama: {total_average:.2f}")

    if final_exam < 50:
        print("Final notun 50'nin altında olduğu için kaldın.")
    elif total_average >= 50:
        print("Dersi geçtin.")
    else:
        print("Dersi geçemedin.")

fightin_calculate_grade()
