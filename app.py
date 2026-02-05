import streamlit as st
st.write("Колко е 2+2")
answer1 = st.number_input("Въведи отговор")
if(answer1 == 4):
  st.write("Правилно")
else:
  st.write("Неправилно")
st.write("Откъде изгрява слънцето")
answer2 = st.text_input("Въведи отговор")
if(answer2 == "изток"):
  st.write("Правилно")
else:
  st.write("Неправилно")
st.write("Какъв цвят е небето")
answer3 = st.text_input("Въведи отговор")
if(answer3 == "синьо"):
  st.write("Правилно")
else:
  st.write("Неправилно")

if(answer1 == true and answer2 == true and answer3 == true):
  st.write("Всичко ти е правилно")
