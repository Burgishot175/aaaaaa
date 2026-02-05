import streamlit as st
st.write("Колко е 2+2")
answer1 = st.num_input()
if(answer1 == 4):
  st.write("Правилно")
