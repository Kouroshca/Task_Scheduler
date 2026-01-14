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

def predict_spam(message):
    """
    Takes a message string, transforms it using the vectorizer,
    and returns the model's prediction.
    """
    # 1. Transform the input text into the format the model expects
    data = vectorizer.transform([message])
    
    # 2. Make the prediction
    prediction = model.predict(data)
    
    # 3. Return the result (usually 0 for ham, 1 for spam)
    return prediction[0]