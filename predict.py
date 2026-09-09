import joblib
import pandas as pd 

model=joblib.load("house_price_model.pkl")

new_house=pd.DataFrame({
    "area":[1000],
    "bedrooms":[2],
    "bathrooms":[1],
    "floors":[3],
    "parking":[1],
    "age":[5],
    "location_score":[8]
})
prediction=model.predict(new_house)
print(f"Predicted House Price: ₹{prediction[0]:,.2f}")

