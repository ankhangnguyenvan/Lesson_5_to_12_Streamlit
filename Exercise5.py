import streamlit as st

with st.form(key='My form', clear_on_submit=True):
    st.write("Form")
    st.text_input("Text here")
    submitted = st.form_submit_button(label='Submit')
    if submitted:
        st.write("Submitted")

st.write("Outside form")


color = ["Green", "Orange", "Red", "Blue", "Yellow"]
option = st.multiselect("Your favourite color", color)

st.write("Your favourite color is: ")
for i in range(len(option)):
    st.write(option[i])

print(type(option))

