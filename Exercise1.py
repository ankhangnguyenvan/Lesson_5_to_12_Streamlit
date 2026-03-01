import streamlit as st
import time

st.title("Introduction myself")
name = st.text_input("Name:  ")
dob = st.text_input("DoB: ")
subject = st.text_input("Favourite subject: ")
hobby = st.text_input("Hobbies: ")

submitButton = st.button("Submit")
if submitButton:
    myBar = st.progress(0)
    for percentComplete in range(100):
        time.sleep(0.05)
        myBar.progress(percentComplete + 1)
    st.balloons()
    st.write(name)
    st.write(dob)
    st.write(subject)
    st.write(hobby)