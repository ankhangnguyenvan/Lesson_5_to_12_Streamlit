import streamlit as st

st.set_page_config(page_title="Personality Test",
                   page_icon=":question",
                   layout="wide",
                   initial_sidebar_state="expanded")
st.title("Let's choose your favourite animal")
col1, col2, col3, col4, col5 = st.columns(5)
Personality = {
    'Cat': 'This choice shows that you are not ready to start work yet, you long for a vacation.',
    'Dog': 'You feel the enthusiastic support of friends and therefore are ready to solve any problems that arise.',
    'Lion': 'It can be seen that you have an outstanding appearance. You attract people with your glamour.',
    'Horse': 'Something is currently limiting your freedom.',
    'Swan': 'At present you are having a sweet time, try to enjoy and prolong it.'
}

with col1:
    b1 = st.button("Cat")
with col2:
    b2 = st.button("Dog")
with col3:
    b3 = st.button("Lion")
with col4:
    b4 = st.button("Horse")
with col5:
    b5 = st.button("Swan")

def showPersonality(animal):
    st.balloons()
    with st.expander(animal):
        st.write(Personality[animal])

if b1:
    showPersonality("Cat")
if b2:
    showPersonality("Dog")
if b3:
    showPersonality("Lion")
if b4:
    showPersonality("Horse")
if b5:
    showPersonality("Swan")

def showSidebar(b, animal):
    if b:
        st.write(f"You have chosen {animal}")

with st.sidebar:
    st.title("Personality Quiz")
    showSidebar(b1, "Cat")
    showSidebar(b2, "Dog")
    showSidebar(b3, "Lion")
    showSidebar(b4, "Horse")
    showSidebar(b5, "Swan")