import math
import streamlit as st


def build_payload():

    applicant_income = st.session_state.get("applicant_income", 0.0)
    coapplicant_income = st.session_state.get("coapplicant_income", 0.0)

    total_income = applicant_income + coapplicant_income

    loan_amount = st.session_state.get("loan_amount", 0.0)

    dependents = st.session_state.get("dependents", 0)

    income_per_dependent = total_income / (dependents + 1)

    loan_term = st.session_state.get("loan_term", 360)

    emi = 0

    if loan_term > 0:
        emi = loan_amount / loan_term

    loan_ratio = 0

    if total_income > 0:
        loan_ratio = loan_amount / total_income

    payload = {

        "Gender_Male":
            1 if st.session_state.get("gender", "Select") == "Male" else 0,

        "Married_Yes":
            1 if st.session_state.get("marital_status", "Select") == "Married" else 0,

        "Dependents":
            dependents,

        "Education_Not_Graduate":
            1 if st.session_state.get("education", "Select") == "Not Graduate" else 0,

        "Self_Employed_Yes":
            1 if st.session_state.get("employment_status", "No") == "Yes" else 0,

        "ApplicantIncome":
            applicant_income,

        "CoapplicantIncome":
            coapplicant_income,

        "LoanAmount":
            loan_amount,

        "Loan_Amount_Term":
            loan_term,

        "Credit_History":
            1 if st.session_state.get("credit_history", "Yes") == "Yes" else 0,

        "Property_Area_Semiurban":
            1 if st.session_state.get("property_area", "Select") == "Semiurban" else 0,

        "Property_Area_Urban":
            1 if st.session_state.get("property_area", "Select") == "Urban" else 0,

        "TotalIncome":
            total_income,

        "LogIncome":
            math.log(total_income + 1),

        "LogLoanAmount":
            math.log(loan_amount + 1),

        "EMI":
            emi,

        "LoanToIncomeRatio":
            loan_ratio,

        "IncomePerDependent":
            income_per_dependent,
    }

    return payload