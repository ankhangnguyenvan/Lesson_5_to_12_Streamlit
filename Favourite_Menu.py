import streamlit as st

def showSelection(text, option):
    st.write(f"**{text}:**")
    if len(option) == 0:
        st.write("You haven't selected any dish.")
    else:
        for i in range(len(option)):
            st.write(option[i])



st.title("Favourite Menu")

appetizer = ["bruschetta", "deviled eggs", "shrimp cocktail"]
mainDishes = ["Italian Pizza Napoletana", "Bolognese pasta", "creamy Carbonara"]
dessert = ["Italian Tiramisu", "French Chocolate Soufflé", "Vietnamese Chè"]

with st.form(key='Favourite Menu'):
    option1 = st.multiselect("Select a Appetizer", appetizer)
    option2 = st.multiselect("Select a Main Dishes", mainDishes)
    option3 = st.multiselect("Select a Dessert", dessert)
    submitted = st.form_submit_button("Submit")
    if submitted:
        showSelection("1. Appetizer", option1)
        showSelection("2. Main dish", option2)
        showSelection("3. Dessert", option3)

