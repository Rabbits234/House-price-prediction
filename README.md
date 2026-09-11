# House Price Prediction

This is my first Machine Learning project. It is a beginner-level project where I built a simple model to predict house prices based on different property features.

## About the Project

The project uses Linear Regression to predict the estimated price of a house.

The dataset contains features such as:

* Area (sq ft)
* Bedrooms
* Bathrooms
* Floors
* Parking Spaces
* Property Age
* Location Score

I also made a simple Streamlit web app where users can enter the property details and get a predicted house price.

## Model

**Algorithm:** Linear Regression

The dataset is split into:

* 80% Training Data
* 20% Testing Data

The model achieved:

* **R² Score:** 98.39%
* **Mean Absolute Error (MAE):** ₹5.72 Lakh

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Matplotlib
* Seaborn

## Project Structure

```text
House-price-prediction/
│
├── app.py
├── train.py
├── predict.py
├── fake_data.py
├── data.csv
├── house_price_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── config.toml
```

This is a beginner project that I built to understand the basic Machine Learning workflow, from creating the dataset and training a model to making predictions through a simple web app.
