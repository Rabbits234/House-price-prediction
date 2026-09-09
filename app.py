import streamlit as st
import joblib
import pandas as pd


st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏡",
    layout="wide"
)


model = joblib.load("house_price_model.pkl")


st.markdown("""
<style>
.stApp {
    background-color: #F7F4E9;
}

h1, h2, h3 {
    color: #285C59;
}

p, label {
    color: #356966 !important;
}

div[data-testid="stNumberInput"] input {
    background-color: #FFFDF4 !important;
    border: 1.5px solid #B9DED5 !important;
    border-radius: 12px !important;
    color: #285C59 !important;
}

.stButton {
    display: flex;
    justify-content: center;
}

.stButton > button {
    width: 250px !important;
    height: 60px !important;
    background-color: #69A99B !important;
    color: white !important;
    border: none !important;
    border-radius: 15px !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

.stButton > button p {
    color: white !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

.stButton > button:hover {
    background-color: #4F9284 !important;
}
</style>
""", unsafe_allow_html=True)


st.title("🏡 House Price Predictor")
st.write("Enter the property details to predict its price.")

st.divider()

st.subheader("Property Details")


col1, col2 = st.columns(2)

with col1:
    area = st.number_input(
        "Area (sq ft)",
        min_value=500,
        value=1000
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        value=2
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        value=1
    )

    floors = st.number_input(
        "Floors",
        min_value=1,
        value=1
    )


with col2:
    parking = st.number_input(
        "Parking Spaces",
        min_value=0,
        value=1
    )

    age = st.number_input(
        "Property Age (years)",
        min_value=0,
        value=5
    )

    location_score = st.number_input(
        "Location Score (1-10)",
        min_value=1,
        max_value=10,
        value=8
    )


st.write("")


if st.button("Predict House Price"):

    new_house = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "floors": [floors],
        "parking": [parking],
        "age": [age],
        "location_score": [location_score]
    })

    prediction = model.predict(new_house)[0]

    st.success(
        f"🏠 Estimated House Price: ₹{prediction:,.0f}"
    )

    