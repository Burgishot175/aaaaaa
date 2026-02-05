import streamlit as st
st.write("Колко е 2+2")
answer1 = int(st.number_input())
if(answer1 == 4):
  st.write("Правилно")
