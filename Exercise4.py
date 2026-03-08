import streamlit as st

st.set_page_config(
    page_title = "Lesson 8",
    page_icon = "images.jpg",
    layout = "wide",
    initial_sidebar_state = "expanded",
)

st.title("Lesson 8")

st.sidebar.title("Lesson 8")
with st.sidebar:
    st.write("item1")
    st.write("item2")
with st.sidebar.expander(":question:"):
    st.write("item4")

col1, col2, col3 = st.columns(3, gap="xxlarge")
with col1:
    st.header("JavaScript")
    st.image("D:\PythonPro4\Lesson_5_to_12_Streamlit\Media\javascript.png")
    st.link_button("JavaScript", "https://www.javascript.com/")
with col2:
    st.header("Python")
    st.image(r"Media\python.png")
    st.link_button("Python", "https://www.python.org/")
with col3:
    st.header("Java")
    st.image("D:\\PythonPro4\\Lesson_5_to_12_Streamlit\\Media\\java.png")
    st.link_button("Java", "https://www.java.com/")

audio = st.audio("D:\PythonPro4\Lesson_5_to_12_Streamlit\Media\Billie Jean - Michael Jackson - Thriller - Michael Jackson - Playlist NhacCuaTui.mp3",
                 "MP3")

video = st.video("https://www.youtube.com/watch?v=kBX5WH9b4M4&pp=ugUEEgJlbg%3D%3D")