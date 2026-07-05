import streamlit as st

def load_css():
    st.markdown("""
    <style>

    .main {
        background-color: #f5f7fb;
    }

    .title {
        text-align: center;
        color: #0E4C92;
        font-size: 42px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #555555;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .approved {
        background:#d4edda;
        color:#155724;
        padding:18px;
        border-radius:12px;
        text-align:center;
        font-size:22px;
        font-weight:bold;
    }

    .rejected {
        background:#f8d7da;
        color:#721c24;
        padding:18px;
        border-radius:12px;
        text-align:center;
        font-size:22px;
        font-weight:bold;
    }

    .footer{
        text-align:center;
        color:gray;
        margin-top:40px;
        font-size:14px;
    }

    </style>
    """, unsafe_allow_html=True)

import requests
import numpy as np

st.set_page_config(
    page_title="Loan Eligibility Predictor",
    page_icon="🏦"
)

load_css()
# Sidebar
st.sidebar.title("🏦 Loan Predictor")

st.sidebar.info(
    """
This application predicts whether a loan is likely to be approved using a Machine Learning model.

### Tech Stack
- Python
- Scikit-learn
- FastAPI
- Streamlit
"""
)

st.sidebar.success("Model: Random Forest")
st.markdown(
    """
    <div class="title">
        🏦 Loan Eligibility Prediction Platform
    </div>

    <div class="subtitle">
        AI-Powered Loan Approval Recommendation System
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

left, right = st.columns(2, gap="large")

with left:
    with st.container(border=True):
        st.subheader("👤 Applicant Details")
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    married = st.selectbox(
        "Marital Status",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        [0,1,2,3]
    )

    education = st.selectbox(
        "Education",
        ["Graduate","Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["No","Yes"]
    )
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    with st.container(border=True):
        st.subheader("🏦 Loan Details")
    applicant_income = st.number_input(
        "Applicant Income",
        min_value=0.0
    )

    coapplicant_income = st.number_input(
        "Coapplicant Income",
        min_value=0.0
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0.0
    )

    loan_term = st.selectbox(
        "Loan Term",
        [360,180,120,84,60,36]
    )

    credit_history = st.selectbox(
        "Credit History",
        [1,0]
    )

    property_area = st.selectbox(
        "Property Area",
        ["Urban","Semiurban","Rural"]
    )


st.divider()

_, center, _ = st.columns([1,2,1])

with center:

    predict = st.button(
        "🔍 Predict Loan Eligibility",
        use_container_width=True
    )

if predict:

    total_income = applicant_income + coapplicant_income

    if total_income <= 0:
        st.error("Total income must be greater than 0.")
        st.stop()

    payload = {
        "Gender_Male": 1 if gender == "Male" else 0,
        "Married_Yes": 1 if married == "Yes" else 0,
        "Dependents": dependents,
        "Education_Not_Graduate": 1 if education == "Not Graduate" else 0,
        "Self_Employed_Yes": 1 if self_employed == "Yes" else 0,

        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,

        "Property_Area_Semiurban": 1 if property_area == "Semiurban" else 0,
        "Property_Area_Urban": 1 if property_area == "Urban" else 0,

        "TotalIncome": total_income,
        "LogIncome": np.log1p(total_income),
        "LogLoanAmount": np.log1p(loan_amount),
        "EMI": loan_amount / loan_term,
        "LoanToIncomeRatio": loan_amount / total_income,
        "IncomePerDependent": total_income / (dependents + 1)
    }

    with st.spinner("Predicting..."):

        try:
            response = requests.post(
                "https://loan-eligibility-api-bj5j.onrender.com/predict",
                json=payload
            )

            if response.status_code == 200:

                result = response.json()

                st.subheader("📊 Prediction Result")

                if result["loan_approved"]:
                    st.markdown(
                        """
                        <div class="approved">
                        🎉 LOAN APPROVED
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        """
                        <div class="rejected">
                        ❌ LOAN REJECTED
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # Confidence message
                prob = result["approval_probability"]

                if prob >= 85:
                    st.success("🟢 Very High Chance of Approval")
                elif prob >= 70:
                    st.info("🟡 Good Chance of Approval")
                elif prob >= 50:
                    st.warning("🟠 Borderline Approval")
                else:
                    st.error("🔴 Low Chance of Approval")

                st.progress(prob / 100)

                st.metric(
                    "Approval Probability",
                    f"{prob}%"
                )

                st.divider()

                st.subheader("📋 Applicant Summary")

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**Total Income:** ₹ {total_income:,.0f}")
                    st.write(f"**Loan Amount:** ₹ {loan_amount:,.0f}")
                    st.write(f"**Loan Term:** {loan_term} months")

                with col2:
                    st.write(f"**Credit History:** {credit_history}")
                    st.write(f"**Property Area:** {property_area}")
                    st.write(f"**Dependents:** {dependents}")

            else:
                st.error("❌ Unable to connect to the FastAPI server.")
               

        except Exception as e:
            st.error(f"Error: {e}")
st.markdown(
    """
    <hr>

    <div class="footer">
        Developed by <b>Drishti Saha</b> • Powered by FastAPI + Streamlit + Scikit-learn
    </div>
    """,
    unsafe_allow_html=True
)

