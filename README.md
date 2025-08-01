
## Freelancer Earnings Estimator
A Flask-based web application that predicts a freelancer’s estimated earnings based on key input factors such as skills, experience, rating, number of projects, and location. Powered by Linear Regression.

## Table of Contents
        Overview

        Demo

        Features

        Tech Stack

        Installation

        Usage

        Project Structure

        Dataset

        Screenshots

        License
    ---

## Overview

   This project uses Linear Regression to predict freelance earnings. It's designed for freelancers or platforms that want quick and reliable income estimates based on various parameters like skills, experience, ratings, and client history.

---
## Project Structure
```
freelancer-earnings-estimator/
│
├── app.py                  # Main Flask app
├── model_train.py          # Model training script
├── freelancer_dataset.csv  # Dataset file
├── earnings_model.pkl      # Saved regression model
├── templates/
│   └── index.html          # Frontend HTML
├── static/
│   └── style.css           # Custom CSS styling
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```
## Accepts key freelancer input fields like:

    Experience (years)

    Rating (1-5)

    Completed Projects

    Location

    Skill Category

    Uses a preprocessed dataset for accurate results
    ---

## Tech Stack
        Technology	Use
        Python	Core language
        Flask	Web framework
        scikit-learn	ML modeling
        HTML/CSS	Frontend
        Bootstrap	Styling (optional)
        Pandas	Data handling
        NumPy	Numerical operations

## Installation
Clone the repo and install dependencies:
```
 git clone https://github.com/Deepakprasath10/Linear.git
 cd freelancer-earnings-estimator
 pip install -r requirements.txt
```
Train the model:
```
python model_train.py
```

Run the Flask server:

```
python app.py
```
Open your browser and go to:

http://127.0.0.1:5000/

##  Dataset
Format: CSV (freelancer_dataset.csv)

Sample Columns:

experience: float — Years of freelancing experience

rating: float — Freelancer platform rating

projects: int — Number of completed projects

location: string — Freelancer's location

category: string — Type of freelance work

earning: float — Actual earning (target variable)

(You can use dummy or synthetic data for experimentation.)

## Screenshots

![alt text](<Screenshot 2025-08-01 185454.png>)
![alt text](<Screenshot 2025-08-01 185519.png>)
![alt text](<Screenshot 2025-08-01 185528.png>)