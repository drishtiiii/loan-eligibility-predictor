# 🏦 Loan Eligibility Prediction Platform

An end-to-end Machine Learning web application that predicts whether a loan application is likely to be approved based on applicant information.

The project demonstrates the complete Machine Learning lifecycle including data preprocessing, feature engineering, model training, REST API development using FastAPI, and an interactive frontend built with Streamlit.

---
## 🌐 Live Demo


🚀 **Web App:**  
https://loan-eligibility-predictor.streamlit.app


📖 **API Documentation:**  
https://loan-eligibility-api-bj5j.onrender.com/docs

💻 **Source Code:**  
https://github.com/drishtiiii/loan-eligibility-predictor

# 📌 Features

- Predicts loan approval using a trained Machine Learning model
- FastAPI backend with REST API
- Interactive Streamlit frontend
- Feature engineering for better prediction accuracy
- Approval probability score
- Applicant summary dashboard
- Swagger API documentation
- Clean and responsive user interface

---

# 🚀 Tech Stack

## Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn

## Backend

- FastAPI
- Uvicorn
- Pydantic

## Frontend

- Streamlit

## Model Serialization

- Joblib

---

# 📂 Project Structure

```
loan-eligibility-predictor/
│
├── app/
│   ├── config.py
│   ├── inference.py
│   ├── main.py
│   ├── preprocess.py
│   └── schemas.py
│
├── artifacts/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── feature_columns.pkl
│
├── data/
│   ├── train.csv
│   └── processed_loan_data.csv
│
├── notebooks/
│   └── EDA.ipynb
│
├── screenshots/
│
├── tests/
│
├── requirements.txt
├── streamlit_app.py
├── Dockerfile
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/drishtiiii/loan-eligibility-predictor.git
```

Move into the project

```bash
cd loan-eligibility-predictor
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run FastAPI

```bash
python -m uvicorn app.main:app --reload
```

FastAPI will run at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit

```bash
streamlit run streamlit_app.py
```

---

# 📸 Screenshots

## Streamlit Dashboard

![Dashboard](screenshots/dashboard.png)

---

## Prediction Result

![Prediction](screenshots/prediction.png)

---

## Swagger API

![Swagger](screenshots/swagger.png)

---

# 📊 Machine Learning Pipeline

1. Data Cleaning
2. Missing Value Handling
3. Feature Engineering
4. Feature Scaling
5. Model Training
6. Model Evaluation
7. Model Serialization
8. API Development
9. Streamlit Integration

---

# 📈 Engineered Features

The application automatically generates:

- Total Income
- Log Income
- Log Loan Amount
- EMI
- Loan-to-Income Ratio
- Income per Dependent

These engineered features improve the predictive performance of the model.

---

# 🧪 API Endpoint

### POST

```
/predict
```

Example Request

```json
{
  "Gender_Male": 1,
  "Married_Yes": 1,
  "Dependents": 1,
  "Education_Not_Graduate": 0,
  "Self_Employed_Yes": 0,
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 2000,
  "LoanAmount": 120,
  "Loan_Amount_Term": 360,
  "Credit_History": 1,
  "Property_Area_Semiurban": 1,
  "Property_Area_Urban": 0,
  "TotalIncome": 7000,
  "LogIncome": 8.85,
  "LogLoanAmount": 4.79,
  "EMI": 0.33,
  "LoanToIncomeRatio": 0.017,
  "IncomePerDependent": 3500
}
```

Example Response

```json
{
  "loan_approved": true,
  "approval_probability": 71.5
}
```

---

# 🔮 Future Improvements

- Explainable AI using SHAP
- Docker deployment
- Cloud deployment
- CI/CD using GitHub Actions
- User Authentication
- Database integration
- Loan recommendation engine

---

# 👩‍💻 Author

**Drishti Saha**

GitHub:
https://github.com/drishtiiii

