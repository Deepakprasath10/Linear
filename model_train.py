import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load data
df = pd.read_csv("linear.csv")

# Features & target
X = df.drop("Project_Price", axis=1)
y = df["Project_Price"]

# Preprocessing
categorical = ["Experience_Level", "Category", "Country"]
numeric = ["Reviews", "Rating"]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(drop="first"), categorical)
], remainder="passthrough")

model = Pipeline([
    ("preprocess", preprocessor),
    ("regressor", LinearRegression())
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully.")
