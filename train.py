import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score
import joblib

df=pd.read_csv("data.csv")

X=df[[
    "area",
    "bedrooms",
    "bathrooms",
    "floors",
    "parking",
    "age",
    "location_score"
]]
Y=df["price"]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=56)

model=LinearRegression()
model.fit(X_train,Y_train)
prediction=model.predict(X_test)

mae=mean_absolute_error(Y_test,prediction)
r2=r2_score(Y_test,prediction)

print("Model trained successfully!")
print(f"Mean Absolute Error: ₹{mae:,.2f}")
print(f"R² Score: {r2:.4f}")

joblib.dump(model,"house_price_model.pkl")
print ("Model saved successfully")