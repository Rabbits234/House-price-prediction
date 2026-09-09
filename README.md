# 🏠 House Price Prediction

A beginner-friendly Machine Learning project that predicts house prices based on different property features.

## 📌 About the Project

This project uses **Linear Regression** to predict the estimated price of a house.

The model is trained on a synthetic dataset containing property details such as:

- Area (sq ft)
- Bedrooms
- Bathrooms
- Floors
- Parking Spaces
- Property Age
- Location Score

The project also includes a simple **Streamlit web application** where users can enter property details and get a predicted house price.

## 🤖 Machine Learning Model

**Algorithm:** Linear Regression

The dataset is divided into:

- **80% Training Data**
- **20% Testing Data**

The model is evaluated using:

- **R² Score:** 98.39%
- **Mean Absolute Error (MAE):** ₹5.72 Lakh

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib
- Seaborn

## 📂 Project Structure

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