# Ensemble Modeling for Stock Price Prediction

## Objective

To predict stock closing prices using ensemble machine learning techniques and compare the performance of different regression models.

---

## Problem Statement

Accurate stock price prediction is valuable for investors and analysts. This project develops a machine learning pipeline that predicts the closing price using historical stock attributes.

---

## Dataset

Features:

- Open
- High
- Low
- Volume

Target:

- Close

---

## Data Preprocessing

- Removed Date column
- Removed Adjusted Close
- Selected input features
- Train-Test Split

---

## Models

### Linear Regression

R² Score: 0.999937

### Random Forest

R² Score: 0.999879

### Gradient Boosting

R² Score: 0.999829

### Voting Regressor

R² Score: 0.999905

---

## Visualizations

- Actual vs Predicted
- Feature Importance
- Model Comparison

---

## Streamlit Application

Users enter:

- Open Price
- High Price
- Low Price
- Volume

The application predicts the closing stock price.

---

## Conclusion

The project demonstrates how ensemble learning can be applied to stock price prediction using multiple regression models.

---

## Future Scope

- Live market data
- LSTM and Transformer models
- Portfolio prediction
- Financial dashboard