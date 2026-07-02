import pickle
import pandas as pd

with open("MODELS/stock_ensemble_model.pkl", "rb") as file:
    model = pickle.load(file)

def predict_price(input_data):

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)

    return float(prediction[0])