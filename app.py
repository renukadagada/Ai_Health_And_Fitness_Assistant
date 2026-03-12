import streamlit as st
import joblib
import numpy as np

model = joblib.load("fitness_model.pkl")

st.title("AI Health & Fitness Assistant")

age = st.number_input("Age")
height = st.number_input("Height (cm)")
weight = st.number_input("Weight (kg)")
duration = st.number_input("Exercise Duration (minutes)")
heart_rate = st.number_input("Heart Rate")

if st.button("Predict Calories Burned"):
    
    data = np.array([[age, height, weight, duration, heart_rate]])
    
    prediction = model.predict(data)
    
    st.success(f"Estimated Calories Burned: {prediction[0]:.2f}")
