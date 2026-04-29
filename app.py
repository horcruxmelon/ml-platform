from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "Model API running"}

@app.post("/predict")
def predict(number: int):
    prediction = model.predict(np.array([[number]]))[0]
    return {"prediction": int(prediction)}
