import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 House Price Prediction")

st.write("Enter the details below:")

# Inputs (8 features)
area = st.number_input("Area (sq ft)", min_value=0)
bedrooms = st.number_input("Bedrooms", min_value=0)
bathrooms = st.number_input("Bathrooms", min_value=0)
stories = st.number_input("Stories", min_value=0)
parking = st.number_input("Parking", min_value=0)

mainroad = st.selectbox("Main Road (0 = No, 1 = Yes)", [0, 1])
guestroom = st.selectbox("Guest Room (0 = No, 1 = Yes)", [0, 1])
basement = st.selectbox("Basement (0 = No, 1 = Yes)", [0, 1])

# Prediction
if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms, stories, parking, mainroad, guestroom, basement]])
    
    prediction = model.predict(features)
    
    st.success(f"Predicted Price: ₹ {prediction[0]:,.2f}")