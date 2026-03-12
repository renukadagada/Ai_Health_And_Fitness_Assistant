import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

np.random.seed(42)
rows = 5000

data = pd.DataFrame({
    "Age": np.random.randint(18, 60, rows),
    "Gender": np.random.randint(0, 2, rows),
    "Height": np.random.randint(150, 200, rows),
    "Weight": np.random.randint(50, 100, rows),
    "BMI": np.random.uniform(18, 35, rows),
    "Resting_HR": np.random.randint(55, 90, rows),
    "Exercise_Type": np.random.randint(0, 5, rows),
    "Duration": np.random.randint(10, 90, rows),
    "Intensity": np.random.randint(0, 3, rows),
    "Heart_Rate": np.random.randint(90, 170, rows),
    "Steps": np.random.randint(2000, 15000, rows),
    "Sleep": np.random.uniform(5, 9, rows),
    "Water": np.random.uniform(1, 4, rows),
    "Goal": np.random.randint(0, 3, rows)
})

data["Calories"] = (
    data["Duration"] * 5 +
    data["Intensity"] * 40 +
    (data["Heart_Rate"] - 80) * 2 +
    data["Weight"] * 0.5 +
    np.random.normal(0, 20, rows)
)

X = data.drop("Calories", axis=1)
y = data["Calories"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=200)
model.fit(X_train, y_train)

joblib.dump(model, "health_model.pkl")

print("Model created successfully")
