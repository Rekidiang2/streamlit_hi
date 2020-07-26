import streamlit as st


st.title("Hello World")
st.write("Welcome to my first streamlit application!")


st.sidebar.title("Food Survey :smile:")


yogurt = st.sidebar.multiselect("Which do you like the most?",
                                ("Vanilla Yogurt","Berry Yogurt","Greek Yogurt"))


breakfast = st.sidebar.multiselect("Which do you like the most?",
                                ("Toast","Coffee","Weet-bix"))


fruits = st.sidebar.multiselect("Which do you like the most?",
                                ("Strawberry","Raspberry","Cherry"))


st.write("{} is your favourite type of yogurt".format(', '.join(yogurt)))
st.write("{} is your favourite type breakfast".format(', '.join(breakfast)))
st.write("{} is your favourite type of fruit".format(', '.join(fruits)))