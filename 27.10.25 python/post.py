# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 20:30:57 2025

@author: ARIBİLGİ
"""

import streamlit as st 
import requests
url = "https://api.zippopotam.us/tr/09000"
respons = requests.get(url)
data = respons.json()

st.title(data["country"])
st.title(data["post code"])