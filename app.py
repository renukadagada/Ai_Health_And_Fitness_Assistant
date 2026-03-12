import streamlit as st
import numpy as np
import pickle
from diet_plan import diet
from workout_plan import workout
from recommendation import recommend

model = pickle.load(open("health_model.pkl", "rb"))

st.title("AI Health & Fitness Assistant")

# Input fields
inputs = [
    ("Age", int), ("Gender", int), ("Height", int), ("Weight", int),
    ("BMI", float), ("Heart_Rate", int), ("Blood_Pressure", int),
    ("Sleep_Hours", int), ("Daily_Steps", int), ("Calories_Intake", int),
    ("Water_Intake", float), ("Exercise_Minutes", int), ("Stress_Level", int),
    ("Cholesterol", int), ("Sugar_Level", int), ("Smoking", int), ("Alcohol", int),
    ("Screen_Time", int), ("Protein_Intake", int), ("Carbs_Intake", int)
]

user_data = []
for name, dtype in inputs:
    if dtype == int:
        val = st.number_input(name, step=1)
    else:
        val = st.number_input(name, step=0.1)
    user_data.append(val)

if st.button("Analyze Health"):
    data = np.array([user_data])
    prediction = model.predict(data)[0]
    st.subheader("Fitness Level & Recommendation")
    st.write(recommend(prediction))
    st.subheader("Diet Plan")
    st.write(diet(prediction))
    st.subheader("Workout Plan")
    st.write(workout(prediction))