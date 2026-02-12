import streamlit as st
st.write("Кога е почнала втората световна война?")
answer1 = st.number_input("Въведи отговор")

st.write("Кога е свършила втората световна война?")
answer2 = st.text_input("Въведи отговор")

st.write("Кога е създадена България")
answer3 = st.text_input("Въведи oтговор")

st.write("Кога почва първата световна война?")
answersss4 = st.text_input("Въведи oтговор")

st.button("Проверка")
if(answer1 == "1938" and answer2 == "1945" and answer3 == "681" and answersss4 == "1914"):
  st.success("Всичко е правилно")
else:
  st.error("Имаш грешка")
