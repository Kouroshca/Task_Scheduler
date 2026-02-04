# ml_model.py
import pickle
import numpy as np
import os

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "bmi_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def predict_bmi_category(height_cm, weight_kg):
    x = np.array([[height_cm, weight_kg]])
    pred = model.predict(x)[0]
    conf = max(model.predict_proba(x)[0])
    return pred, round(conf * 100, 2)
