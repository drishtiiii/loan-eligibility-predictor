import joblib

from app.config import MODEL_PATH
from app.preprocess import preprocess

# Load trained model
model = joblib.load(MODEL_PATH)

# 👇 ADD THIS
print("========== MODEL FEATURES ==========")
print(list(model.feature_names_in_))
print("====================================")


def predict(data: dict):

    processed_data = preprocess(data)

    prediction = model.predict(processed_data)[0]
    probability = model.predict_proba(processed_data)[0][1]

    return {
        "loan_approved": bool(prediction),
        "approval_probability": round(probability * 100, 2)
    }