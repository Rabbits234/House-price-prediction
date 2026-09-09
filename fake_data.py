import pandas as pd
import numpy as np

np.random.seed(56)

n=1000

area=np.random.randint(500,4000,n)
bedrooms = np.random.randint(1, 6, n)
bathrooms = np.random.randint(1, 5, n)
floors = np.random.randint(1, 4, n)
parking = np.random.randint(0, 4, n)
age = np.random.randint(0, 30, n)
location_score = np.random.randint(1, 11, n)

price=(
    area * 5000
    + bedrooms * 500000
    + bathrooms * 300000
    + floors * 200000
    + parking * 150000
    - age * 50000
    + location_score * 400000
    + np.random.normal(0, 500000, n)
)
df = pd.DataFrame({
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "floors": floors,
    "parking": parking,
    "age": age,
    "location_score": location_score,
    "price": price
})


df.to_csv("data.csv", index=False)
print("Dataset created successfully!")
print(df.head())





