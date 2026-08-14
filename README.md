# AI-Powered Loan Eligibility Predictor

An **AI/ML-powered loan eligibility prediction system** that analyzes applicant, financial, loan, and credit information to predict the likelihood of loan approval.

The application combines a **supervised Machine Learning model**, feature engineering, a **FastAPI inference backend**, and a **Streamlit interactive frontend** to provide an end-to-end AI-powered loan assessment workflow.

> **Note:** This project uses traditional **Artificial Intelligence / Machine Learning** techniques. It does not use Generative AI or an LLM. The prediction intelligence is provided by a trained **Random Forest Classifier**.

---

## 📌 Features

* 📝 Multi-step loan application form
* ✅ Input validation at every step
* 💾 Persistent session state across pages
* 📋 Review application before submission
* 🤖 AI/ML-based loan eligibility prediction
* 🌳 Random Forest classification model
* 🧮 Automated feature engineering
* ⚡ FastAPI backend for ML inference
* 🎨 Clean and responsive Streamlit interface
* 📊 Loan approval probability score
* ☁️ Cloud deployment using Render and Streamlit Community Cloud

---

## 🌐 Live Demo

### 🚀 Frontend

[Loan Eligibility Predictor — Streamlit](https://loan-eligibility-predictor-scqw5frsse7kzfbvpcyq5e.streamlit.app/?utm_source=chatgpt.com)

### ⚡ Backend API

[Loan Eligibility Predictor — FastAPI Backend](https://loan-eligibility-predictor-ksgq.onrender.com/?utm_source=chatgpt.com)

### 📖 API Documentation

[FastAPI Swagger Documentation](https://loan-eligibility-predictor-ksgq.onrender.com/docs?utm_source=chatgpt.com)

---

## 🧠 Artificial Intelligence / Machine Learning

The core intelligence of the application is provided by a **supervised Machine Learning classification model**.

The model is trained on historical loan application data and learns relationships between applicant characteristics and loan approval outcomes.

Instead of using manually defined rules such as:

```text
IF income > threshold
AND credit history = good
THEN approve
```

the Machine Learning model learns patterns from historical examples and applies those learned patterns to new applications.

### AI/ML Pipeline

```text
Applicant Information
        │
        ▼
Data Validation
        │
        ▼
Feature Engineering
        │
        ▼
Feature Transformation
        │
        ▼
Feature Ordering
        │
        ▼
Trained Random Forest Model
        │
        ▼
Loan Prediction
        │
        ├───────────────┐
        ▼               ▼
    Approved         Rejected
        │               │
        └───────┬───────┘
                ▼
       Approval Probability
                │
                ▼
        Display Result
```

The **Random Forest model is the decision-making intelligence layer** of the application.

---

## 🌳 Machine Learning Model

The prediction model is a **Random Forest Classifier** trained on a public Loan Eligibility dataset.

Random Forest is an ensemble Machine Learning algorithm that combines predictions from multiple decision trees to produce a final classification.

For a new applicant:

```text
Applicant Data
      │
      ▼
 ┌─────────────┐
 │ Decision    │
 │ Tree 1      │
 └─────────────┘
      │
 ┌─────────────┐
 │ Decision    │
 │ Tree 2      │
 └─────────────┘
      │
 ┌─────────────┐
 │ Decision    │
 │ Tree 3      │
 └─────────────┘
      │
      ⋮
      │
      ▼
Random Forest Ensemble
      │
      ▼
Final Prediction
      +
Approval Probability
```

The model can capture relationships between multiple applicant and financial features when making its prediction.

> Random Forest was selected as the current production model for this project. Logistic Regression and other classification algorithms could also be evaluated as baselines through model comparison and cross-validation.

---

## 🎯 Problem Statement

Loan eligibility depends on multiple factors, including:

* Applicant income
* Co-applicant income
* Credit history
* Education
* Employment
* Dependents
* Loan amount
* Loan term
* Property area

Analyzing these factors manually can be time-consuming and may result in inconsistent assessments.

This project demonstrates how **Machine Learning can be used as a decision-support system** to analyze historical patterns and generate a loan eligibility prediction.

The system is designed for **educational and demonstration purposes** and does not replace real-world financial underwriting.

---

## 🔄 Application Workflow

```text
User Registration
        │
        ▼
Personal Information
        │
        ▼
Employment & Income
        │
        ▼
Loan Details
        │
        ▼
Credit Assessment
        │
        ▼
Review Application
        │
        ▼
Prepare ML Payload
        │
        ▼
FastAPI Backend
        │
        ▼
Pydantic Validation
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Feature Ordering
        │
        ▼
Random Forest Model
        │
        ▼
Prediction + Probability
        │
        ▼
Streamlit Result
```

---

## 🔬 ML Inference Workflow

Once the user submits the application, the information follows this pipeline:

```text
Raw User Input
      │
      ▼
Streamlit Session State
      │
      ▼
Payload Mapping
      │
      ▼
JSON Request
      │
      ▼
FastAPI /predict
      │
      ▼
Pydantic Schema Validation
      │
      ▼
Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Feature Name Alignment
      │
      ▼
Feature Order Alignment
      │
      ▼
Random Forest Inference
      │
      ├───────────────┐
      ▼               ▼
Prediction       Probability
      │               │
      └───────┬───────┘
              ▼
         JSON Response
              │
              ▼
       Streamlit Result
```

---

## 🧮 Feature Engineering

The application creates additional features from the applicant's raw information before sending the data to the Machine Learning model.

### Total Income

```text
TotalIncome =
ApplicantIncome + CoapplicantIncome
```

### Log Income

```text
LogIncome =
log(TotalIncome + 1)
```

### Log Loan Amount

```text
LogLoanAmount =
log(LoanAmount + 1)
```

### EMI

The application calculates an approximate monthly loan burden using the requested loan amount and loan term.

### Loan-to-Income Ratio

```text
LoanToIncomeRatio =
LoanAmount / TotalIncome
```

### Income Per Dependent

```text
IncomePerDependent =
TotalIncome / (Dependents + 1)
```

These engineered features provide the model with additional information derived from the original applicant data.

---

## 📊 Features Used by the Model

### Applicant Information

* Gender
* Marital Status
* Dependents
* Education
* Self Employment

### Financial Information

* Applicant Income
* Co-applicant Income
* Total Income
* Existing EMI

### Loan Information

* Loan Amount
* Loan Term
* Property Area
* Loan Purpose

### Credit Information

* Credit History
* Previous Loan Information
* Credit Score

---

## 🧠 Why Machine Learning?

The application demonstrates the difference between a traditional rule-based system and a Machine Learning system.

### Traditional Rule-Based Approach

```text
Income > ₹50,000?
       │
       ▼
Credit History = Yes?
       │
       ▼
Loan Amount < Threshold?
       │
       ▼
Approve / Reject
```

These rules have to be manually created.

### Machine Learning Approach

```text
Historical Loan Data
        │
        ▼
Training
        │
        ▼
Machine Learning Model
        │
        ▼
Learned Patterns
        │
        ▼
New Applicant
        │
        ▼
Prediction
```

The ML model learns relationships from historical data instead of relying entirely on manually written decision rules.

---

## 📈 Prediction Output

The model returns:

```json
{
    "loan_approved": true,
    "approval_probability": 82.45
}
```

The output contains:

* **Loan Approval Status**
* **Approval Probability**

The probability is generated using the model's `predict_proba()` output.

---

## 🏗️ System Architecture

```text
                  USER
                   │
                   ▼
        ┌─────────────────────┐
        │ Streamlit Frontend  │
        │                     │
        │ Multi-step Form     │
        │ Session State       │
        │ Review Page         │
        └──────────┬──────────┘
                   │
                   │ JSON
                   ▼
        ┌─────────────────────┐
        │    FastAPI API      │
        │                     │
        │     /predict        │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │ Pydantic Validation │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │   Preprocessing     │
        │ Feature Engineering │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │  Feature Ordering   │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │  Random Forest ML   │
        │       Model         │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │ Prediction +        │
        │ Probability         │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │ Streamlit Result    │
        └─────────────────────┘
```

---

## 🛠 Tech Stack

### 🤖 Artificial Intelligence / Machine Learning

* Python
* Scikit-Learn
* Random Forest Classifier
* Pandas
* NumPy
* Joblib
* Feature Engineering

### ⚡ Backend

* FastAPI
* Pydantic
* Uvicorn
* REST API

### 🎨 Frontend

* Streamlit
* Python
* Streamlit Session State
* Custom CSS

### ☁️ Deployment

* GitHub
* Render
* Streamlit Community Cloud

---

## 📂 Project Structure

```text
loan-eligibility-predictor/
│
├── app/
│   ├── main.py
│   ├── inference.py
│   ├── preprocess.py
│   ├── schemas.py
│   ├── config.py
│   └── model.pkl
│
├── frontend/
│   ├── app.py
│   ├── pages/
│   ├── components/
│   ├── utils/
│   └── assets/
│
├── notebooks/
├── dataset/
├── requirements.txt
└── README.md
```

---

## 📸 Screenshots

### Registration

<p align="center">
<img src="screenshots/registration.png" width="800">
</p>

---

### Personal Information

<p align="center">
<img src="screenshots/personal.png" width="800">
</p>

---

### Employment & Income

<p align="center">
<img src="screenshots/income.png" width="800">
</p>

---

### Loan Details

<p align="center">
<img src="screenshots/loan.png" width="800">
</p>

---

### Credit Assessment

<p align="center">
<img src="screenshots/credit.png" width="800">
</p>

---

### Review Application

<p align="center">
<img src="screenshots/review.png" width="800">
</p>

---

### Prediction Result

<p align="center">
<img src="screenshots/result.png" width="800">
</p>

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/drishtiiii/loan-eligibility-predictor.git

cd loan-eligibility-predictor
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Backend

```bash
python -m uvicorn app.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Frontend

```bash
streamlit run frontend/app.py
```

Frontend runs at:

```text
http://localhost:8501
```

---

## 🔌 API

### `POST /predict`

The Streamlit frontend sends the processed applicant information to the FastAPI backend through the `/predict` endpoint.

The backend:

1. Receives the JSON request.
2. Validates the input using Pydantic.
3. Preprocesses the data.
4. Aligns the feature names and order with the trained model.
5. Performs Random Forest inference.
6. Generates the prediction and probability.
7. Returns a JSON response to the frontend.

---

## 🛡️ Validation & Error Handling

The backend validates incoming requests before performing ML inference.

```text
User Input
    │
    ▼
Pydantic Validation
    │
    ├── Invalid
    │      ↓
    │   HTTP 422
    │
    └── Valid
           ↓
      Preprocessing
           ↓
      ML Prediction
```

This ensures that malformed requests do not directly reach the Machine Learning model.

---

## 🚀 Deployment Architecture

```text
             INTERNET
                 │
        ┌────────┴─────────┐
        │                  │
        ▼                  ▼
 Streamlit Cloud        Render
        │                  │
        ▼                  ▼
  Streamlit UI        FastAPI API
                           │
                           ▼
                    Random Forest
                        Model
                           │
                           ▼
                      Prediction
                           │
                           └──────────► Streamlit
```

The frontend and backend are deployed independently:

* **Streamlit Community Cloud** → User interface
* **Render** → FastAPI inference API
* **GitHub** → Source code repository

---

## 💡 Future Improvements

* 🔐 User Authentication
* 📚 Application History
* 🗄️ Database Integration
* 🔍 Explainable AI using SHAP/LIME
* ⚖️ Logistic Regression vs Random Forest comparison
* 📊 Model performance dashboard
* 🔄 Cross-validation and hyperparameter tuning
* 🐳 Docker Support
* 📈 Model monitoring
* 🔁 Automated model retraining
* ☁️ Improved production deployment

---

## ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes**.

The prediction generated by this application should not be considered an actual financial approval decision.

Real-world lending decisions involve additional factors, regulatory requirements, institutional policies, applicant verification, risk assessment, and human review.

---

## 👩‍💻 Author

**Drishti Saha**

GitHub: [drishtiiii](https://github.com/drishtiiii?utm_source=chatgpt.com)

LinkedIn: [Drishti Saha](https://www.linkedin.com/in/drishti-saha/?utm_source=chatgpt.com)

---

## ⭐ If you like this project

Give the repository a ⭐ on GitHub!
