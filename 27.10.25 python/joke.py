# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 20:13:25 2025

@author: ARIBİLGİ
"""

import streamlit as st
import requests
st.image("smile.jpeg")
st.title("Şaka Makinesi")

if st.button("Yeni Şaka Getir"):
    url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        if data["type"] == "single":
            joke = data["joke"]
        
        else:
            joke = f"{data['setup']} ... {data['delivery']}"
        
        st.success(joke)
    else:
        st.error("Şaka alınırken bir hata oluştu!")
