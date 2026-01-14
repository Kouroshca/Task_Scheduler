import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "spam_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

try:
    model = pickle.load(open(model_path, "rb"))
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

try:
    vectorizer = pickle.load(open(vectorizer_path, "rb"))
except Exception as e:
    raise RuntimeError(f"Failed to load vectorizer: {e}")