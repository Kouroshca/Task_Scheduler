import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "spam_model.pkl")
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

model = pickle.load(open(model_path, "rb"))

def predict_spam(text):
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    probability = max(model.predict_proba(text_vec)[0])

    return prediction, round(probability * 100, 2)