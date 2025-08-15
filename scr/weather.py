import requests
import streamlit as st
from API_reader import iran_cities
st.title("list city")
selected_city = st.selectbox("یک شهر انتخاب کنید:", iran_cities)
if st.button("شروع عملیات"):
    weather = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={selected_city},IR&appid=db3f9e9c1f7a2b07ecc85afa17c33776&units=metric")
    response = weather.json()
    data = response["main"]["temp"],response["main"]["temp_max"],response["main"]["temp_min"]
    st.write(response["weather"][0]["description"],data)
else:
    st.write("برای شروع روی دکمه بالا کلیک کن.")










# print(data)
#  print(data["main"]["temp"])
#  print(data["main"]["feels_like"])
# print(response["sys"]["country"],response["name"])
# # print(response)
# print(iran_cities)