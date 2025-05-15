import streamlit as st
import pickle

st.title("Iris Plant Prediction App")
sl=st.number_input("Sepal-Length")
sw=st.number_input("Sepal-Width")
pl=st.number_input("Petal-Length")
pw=st.number_input("Petal-Width")
button=st.button("Predict Iris Plant")
if button:
    iris=pickle.load(open("iris.pkl","rb"))
    res=iris.predict([[sl,sw,pl,pw]])[0]
    st.markdown(f"Iris Plant: {res}")