import pickle
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "bmi_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def predict_bmi_category(height_cm, weight_kg):
    x = np.array([[height_cm, weight_kg]])
    prediction = model.predict(x)[0]
    confidence = max(model.predict_proba(x)[0])
    return prediction, round(confidence * 100, 2)
