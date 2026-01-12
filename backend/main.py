from fastapi import FastAPI
import requests

app = FastAPI()

MODEL_URL = "http://model-service:8081/predict"

@app.post("/loan")
def loan(data: dict):
    response = requests.post(MODEL_URL, json=data)
    return response.json()
