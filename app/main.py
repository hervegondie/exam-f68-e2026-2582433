from fastapi import FastAPI
from pydantic import BaseModel
from app.utils import predict

app = FastAPI()

class PredictionRequest(BaseModel):
    features: list[float]

@app.post("/predict")
def predict_endpoint(data: PredictionRequest):
    if not data.features:  # liste vide
        return {"predictions": []}
    predictions = predict(data.features)
    return {"predictions": predictions}

@app.get("/")
def read_root():
    return {"message": "API is up and running!"}

@app.get("/favicon.ico")
def favicon():
    return ""
