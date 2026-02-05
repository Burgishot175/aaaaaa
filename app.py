import streamlit as st
st.write("Колко е 2+2")
answer1 = st.number_input("Въведи отговор")

st.write("Откъде изгрява слънцето")
answer2 = st.text_input("Въведи отговор")

st.write("Какъв цвят е небето")
answer3 = st.text_input("Въведи oтговор")


st.button("Проверка")
if(answer1 == 4 and answer2 == "изток" and answer3 == "синьо"):
  st.write("Всичко е правилно")
else:
  st.write("Имаш грешка")
