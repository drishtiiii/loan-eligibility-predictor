from fastapi import FastAPI

from app.schemas import LoanApplication
from app.inference import predict

app = FastAPI(
    title="Loan Eligibility API",
    version="1.0",
)


@app.get("/")
def home():
    return {"message": "Loan Prediction API is running!"}


@app.post("/predict")
def predict_loan(application: LoanApplication):
    result = predict(application.model_dump())
    return result