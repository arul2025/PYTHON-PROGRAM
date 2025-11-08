# PYTHON-PROGRAM

https://arul2025.github.io/PYTHON-PROGRAM/


import streamlit as st

st.title("My First Streamlit App 🎉")

st.write("Hello, welcome to Streamlit!")

st.write("This is a simple interactive web app made with Python.")

# Interactive widgets

name = st.text_input("Enter your name:")

if name:
    st.success(f"Nice to meet you, {name}!")

number = st.slider("Select a number:", 0, 100, 50)
st.write(f"You selected: {number}")
