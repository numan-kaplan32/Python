# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 13:51:44 2025

@author: numan
"""
import streamlit as st

if "carsList" not in st.session_state:
    st.session_state.carsList = {
        "Mercedes": {"price": 1000, "stock": 3},
        "BMW": {"price": 950, "stock": 2},
        "Toyota": {"price": 750, "stock": 4},
        "Fiat": {"price": 600, "stock": 5},
        "Audi": {"price": 1100, "stock": 1},
        "Togg": {"price": 1200, "stock": 3},
        "Volvo": {"price": 900, "stock": 2},
        "Honda": {"price": 800, "stock": 4}
    }

st.set_page_config(page_title="Araba Kiralama Sistemi", layout="wide")
st.title("Araba Kiralama Uygulaması")

st.sidebar.header("Araç Seçimi ve Kira Hesaplama")
selectedCar = st.sidebar.selectbox("Araç Seçiniz:", list(st.session_state.carsList.keys()))
dailyPrice = st.session_state.carsList[selectedCar]["price"]
rentalDays = st.sidebar.number_input("Kaç Gün Kiralayacaksınız?", min_value=1, step=1)

st.sidebar.write(f"{selectedCar} aracının günlük ücreti: {dailyPrice} ₺")
st.sidebar.write(f"Müsait araç adedi: {st.session_state.carsList[selectedCar]['stock']}")

totalPrice = dailyPrice * rentalDays
st.sidebar.write(f"Toplam Kira Bedeli: {totalPrice} ₺")

if st.sidebar.button("Kirala"):
    if st.session_state.carsList[selectedCar]["stock"] > 0 and rentalDays <= st.session_state.carsList[selectedCar]["stock"]:
        st.session_state.carsList[selectedCar]["stock"] -= rentalDays
        st.sidebar.success(f"{selectedCar} başarıyla kiralandı. Kalan araç: {st.session_state.carsList[selectedCar]['stock']}")
    else:
        st.sidebar.warning(f"{selectedCar} kiralanamaz. Stokta araç kalmadı.")

st.header("Kullanıcı Yorumları")

try:
    with open("yorum.txt", "r", encoding="utf-8") as f:
        commentsList = f.readlines()
except FileNotFoundError:
    commentsList = []

with st.form("yorumForm"):
    userName = st.text_input("Adınızı giriniz:")
    userComment = st.text_area("Yorumunuzu yazınız:")
    car = st.selectbox("Araba seçin", list(st.session_state.carsList.keys()))
    submit = st.form_submit_button("Yorumu Kaydet")

    if submit:
        if userName.strip() and userComment.strip():
            with open("yorum.txt", "a", encoding="utf-8") as f:
                f.write(f"{userName}: {userComment} ({car})\n")
            st.success("Yorum kaydedildi")
            commentsList.append(f"{userName}: {userComment} ({car})")
        else:
            st.warning("Adınızı ve yorumunuzu giriniz.")

st.subheader("Önceki Yorumlar")
if commentsList:
    for comment in commentsList[::-1]:
        st.write(comment.strip())
else:
    st.write("Henüz yorum yapılmamış.")

