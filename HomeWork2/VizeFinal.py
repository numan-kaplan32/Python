# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 15:38:27 2025

@author: numan
"""
import streamlit as st

def calculate_score():
    st.title("Vize-Final Not Hesaplama")

    midterm1 = st.number_input("1. Vize Notunu Gir:")
    midterm2 = st.number_input("2. Vize Notunu Gir:")
    final_exam = st.number_input("Final Notunu Gir:")

    if st.button("Hesapla"):
        if 0 <= midterm1 <= 100 and 0 <= midterm2 <= 100 and 0 <= final_exam <= 100:
            midterm_average = (midterm1 + midterm2) / 2
            total_average = (midterm_average * 0.3) + (final_exam * 0.7)
    
            st.write(f"Vize Ortalaması: {midterm_average:.2f}")
            st.write(f"Genel Ortalama: {total_average:.2f}")
    
            if final_exam < 50:
                st.error("Final notun 50'nin altında olduğu için kaldın.")
            elif total_average >= 50:
                st.success("Dersi geçtin.")
            else:
                st.warning("Dersi geçemedin.")
        else:
            st.error("Notlar 0 ile 100 arasında olmalıdır!")

calculate_score()


