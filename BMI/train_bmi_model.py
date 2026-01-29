import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# ----------------------------
# Sample BMI dataset
# [height_cm, weight_kg]
# ----------------------------
X = np.array([
    [170, 50], [165, 48], [180, 55],     # Underweight
    [170, 65], [165, 60], [180, 75],     # Normal
    [170, 80], [165, 78], [180, 90],     # Overweight
    [170, 100], [165, 95], [180, 110]    # Obese
])

y = np.array([
    "Underweight", "Underweight", "Underweight",
    "Normal", "Normal", "Normal",
    "Overweight", "Overweight", "Overweight",
    "Obese", "Obese", "Obese"
])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model
with open("bmi_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ BMI ML model saved as bmi_model.pkl")
