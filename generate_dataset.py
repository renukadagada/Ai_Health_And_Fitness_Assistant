import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000  # number of samples

data = pd.DataFrame({
    "Age": np.random.randint(18, 60, n),
    "Gender": np.random.randint(0, 2, n),  # 0 = Female, 1 = Male
    "Height": np.random.randint(150, 190, n),
    "Weight": np.random.randint(50, 100, n),
    "BMI": np.round(np.random.uniform(18, 35, n), 1),
    "Heart_Rate": np.random.randint(60, 100, n),
    "Blood_Pressure": np.random.randint(110, 150, n),
    "Sleep_Hours": np.random.randint(4, 10, n),
    "Daily_Steps": np.random.randint(2000, 15000, n),
    "Calories_Intake": np.random.randint(1800, 3500, n),
    "Water_Intake": np.round(np.random.uniform(1, 4, n), 1),
    "Exercise_Minutes": np.random.randint(0, 120, n),
    "Stress_Level": np.random.randint(1, 10, n),
    "Cholesterol": np.random.randint(150, 300, n),
    "Sugar_Level": np.random.randint(70, 150, n),
    "Smoking": np.random.randint(0, 2, n),
    "Alcohol": np.random.randint(0, 2, n),
    "Screen_Time": np.random.randint(1, 12, n),
    "Protein_Intake": np.random.randint(30, 120, n),
    "Carbs_Intake": np.random.randint(100, 400, n),
})

# Assign Fitness_Level
def fitness_level(row):
    score = 0
    if row["Daily_Steps"] > 7000: score += 1
    if row["Exercise_Minutes"] > 30: score += 1
    if 18 <= row["BMI"] <= 25: score += 1
    if row["Sleep_Hours"] >= 7: score += 1
    if row["Water_Intake"] >= 2: score += 1
    if row["Stress_Level"] <= 5: score += 1
    if row["Smoking"] == 0: score += 1
    if row["Alcohol"] == 0: score += 1
    if score <= 3: return 0  # Low
    elif score <= 6: return 1  # Medium
    else: return 2  # High

data["Fitness_Level"] = data.apply(fitness_level, axis=1)

# Save CSV
data.to_csv("fitness.csv", index=False)
print("Dataset created: fitness.csv")