import streamlit as st
from SRC.predict import predict_price
from SRC.utils import format_price

st.title("📈 Ensemble Stock Price Predictor")

st.write("Predict Stock Closing Price using Ensemble Learning")

open_price = st.number_input("Open Price", value=150.0)
high_price = st.number_input("High Price", value=155.0)
low_price = st.number_input("Low Price", value=148.0)
volume = st.number_input("Volume", value=5000000)

if st.button("Predict Closing Price"):

    input_data = {
        "Open": open_price,
        "High": high_price,
        "Low": low_price,
        "Volume": volume
    }

    prediction = predict_price(input_data)

    st.metric(
        "Predicted Closing Price",
        format_price(prediction)
    )