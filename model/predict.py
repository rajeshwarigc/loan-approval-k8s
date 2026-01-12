from fastapi import FastAPI
import pickle

app = FastAPI()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(data: dict):
    features = [[
        data["age"],
        data["income"],
        data["credit_score"]
    ]]
    prediction = model.predict(features)[0]
    return {"loan_approved": bool(prediction)}
