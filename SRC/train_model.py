import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    VotingRegressor
)
from sklearn.linear_model import LinearRegression

# Load Dataset
df = pd.read_csv("DATA/apple_stock.csv")   # Replace with your CSV name

# Remove unnecessary columns
df = df.drop(columns=["Date", "Adj Close"])

# Features and Target
X = df.drop(columns=["Close"])
y = df["Close"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Models
lr = LinearRegression()
rf = RandomForestRegressor(n_estimators=100, random_state=42)
gb = GradientBoostingRegressor(random_state=42)

ensemble = VotingRegressor([
    ("lr", lr),
    ("rf", rf),
    ("gb", gb)
])

# Train
ensemble.fit(X_train, y_train)

# Save Model
with open("MODELS/stock_ensemble_model.pkl", "wb") as file:
    pickle.dump(ensemble, file)

print("Model Saved Successfully!")