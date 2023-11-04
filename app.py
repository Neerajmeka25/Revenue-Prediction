import streamlit as st
import pickle

model = pickle.load(open('predict.pkl','rb'))

st.title("Revenue Generator")
st.subheader("This is Machine Learning model that predicts revenue according to the Temperature of the area.")
temp = st.number_input('Enter the Temperature of the area')

if st.button("Predict Revenue"):
    st.subheader("The predicted revenue is: $" + str(int(model.predict([[temp]]))))
