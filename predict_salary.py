# predict_salary.py

import pickle
import pandas as pd

# Function to load the trained model
def load_model():
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

# Function to make predictions
def predict(data):
    model = load_model()
    prediction = model.predict(data)
    return prediction
