import streamlit as st

st.set_page_config(page_title='Exercise 3',
                   page_icon=':smile:', #Xem lại bài 5 để lấy streamlit icon face
                   layout='wide',
                   initial_sidebar_state="collapsed")
st.title("Hello")
st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry."
         " Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"
         " when an unknown printer took a galley of type and scrambled it to make a type specimen book."
         " It has survived not only five centuries, but also the leap into electronic typesetting,"
         " remaining essentially unchanged."
         " It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,"
         " and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum")

with st.expander("Natural Numbers"):
    st.write("1, 2, 3, 4, 5, ...")

col1, col2, col3 = st.columns(3, gap="xxlarge")
with col1:
    st.header("Natural Numbers")
    st.write("1, 2, 3, 4, 5, ...")
with col2:
    st.header("Integer Numbers")
    st.write("1, 2, 3, 4, 5, ...")
with col3:
    st.header("Floating Points")
    st.write("1.1, 2.2, 3.3, 4.4, 5.5, ...")


with st.sidebar:
    st.title("Natural Numbers")
    st.write("Example")
