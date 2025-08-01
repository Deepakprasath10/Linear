from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    experience = request.form["experience"]
    reviews = int(request.form["reviews"])
    rating = float(request.form["rating"])
    category = request.form["category"]
    country = request.form["country"]

    df = pd.DataFrame([[experience, reviews, rating, category, country]],
                      columns=["Experience_Level", "Reviews", "Rating", "Category", "Country"])
    prediction = model.predict(df)[0]
    return render_template("result.html", prediction=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)
