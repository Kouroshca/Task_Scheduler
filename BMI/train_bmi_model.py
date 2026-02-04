import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression

X = np.array([
    [170, 50], [165, 48], [180, 55],
    [170, 65], [165, 60], [180, 75],
    [170, 80], [165, 78], [180, 90],
    [170, 100], [165, 95], [180, 110]
])

y = [
    "Underweight","Underweight","Underweight",
    "Normal","Normal","Normal",
    "Overweight","Overweight","Overweight",
    "Obese","Obese","Obese"
]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

with open("bmi_model.pkl", "wb") as f:
    pickle.dump(model, f)