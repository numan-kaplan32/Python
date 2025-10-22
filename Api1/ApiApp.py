# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 20:54:26 2025

@author: ARIBİLGİ
"""

import json as jsn
import streamlit as st

bookName = st.text_input("Kitabın ismini girin : ")
bookAuthor = st.text_input("Yazar girin : ")
userComment = st.text_area("Yorumunuz : ")
submit = st.button("Ekle")
def addComm():    
    with open("userComments.json","r") as file:
        data = jsn.load(file)
        newId = len(data["comments"]) + 1
        newComment ={
            "id" : newId,
            "name":bookName,
            "nameAuthor" : bookAuthor,
            "comm" : userComment
            }
        data["comments"].append(newComment)
    with open("userComments.json","w",encoding="utf-8") as file:
        jsn.dump(data,file)
if submit:
    addComm()
    st.success("Başarı ile eklendi.")
    st.experimental_rerun()
else:
    st.warning("Eklenemedi")