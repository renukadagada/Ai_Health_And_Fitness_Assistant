import streamlit as st
import joblib
import numpy as np

st.title("AI Health & Fitness Assistant")

# Load model
model = joblib.load("health_model.pkl")

st.header("Enter Your Health Details")

# Personal Information
age = st.number_input("Age", min_value=10, max_value=100)
gender = st.selectbox("Gender", ["Male", "Female"])
height = st.number_input("Height (cm)", min_value=100, max_value=220)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200)

# Health Metrics
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0)
resting_hr = st.number_input("Resting Heart Rate (bpm)", min_value=40, max_value=120)

# Workout Information
exercise_type = st.selectbox(
    "Exercise Type",
    ["Running", "Walking", "Cycling", "Gym", "Yoga"]
)

duration = st.number_input("Workout Duration (minutes)", min_value=5, max_value=180)

intensity = st.selectbox(
    "Workout Intensity",
    ["Low", "Medium", "High"]
)

heart_rate = st.number_input("Heart Rate During Exercise", min_value=60, max_value=200)

# Lifestyle Information
steps = st.number_input("Daily Steps", min_value=0, max_value=30000)
sleep = st.number_input("Sleep Hours", min_value=0.0, max_value=12.0)
water = st.number_input("Water Intake (liters)", min_value=0.0, max_value=5.0)

# Fitness Goal
goal = st.selectbox(
    "Fitness Goal",
    ["Weight Loss", "Muscle Gain", "Maintain Fitness"]
)

# Encode categorical values
gender = 1 if gender == "Male" else 0

exercise_map = {"Running":0,"Walking":1,"Cycling":2,"Gym":3,"Yoga":4}
exercise_type = exercise_map[exercise_type]

intensity_map = {"Low":0,"Medium":1,"High":2}
intensity = intensity_map[intensity]

goal_map = {"Weight Loss":0,"Muscle Gain":1,"Maintain Fitness":2}
goal = goal_map[goal]

# Prediction
if st.button("Predict Fitness Result"):

    data = np.array([[age, gender, height, weight, bmi,
                      resting_hr, exercise_type, duration,
                      intensity, heart_rate, steps,
                      sleep, water, goal]])

    prediction = model.predict(data)

    st.success(f"🔥 Estimated Calories Burned: {prediction[0]:.2f} kcal")

    st.subheader("Workout Recommendation")
    st.write("30 min cardio + 15 min strength training")

    st.subheader("Diet Recommendation")
    st.write("Balanced diet with protein, vegetables, fruits and proper hydration")

    st.subheader("Health Tip")
    st.write("Try to maintain at least 8,000–10,000 steps daily.")
