import math
import streamlit as st


def build_payload():

    applicant_income = st.session_state.applicant_income
    coapplicant_income = st.session_state.coapplicant_income

    total_income = applicant_income + coapplicant_income

    loan_amount = st.session_state.loan_amount

    dependents = st.session_state.dependents
    income_per_dependent = total_income / (dependents + 1)
    emi = 0

    if st.session_state.loan_term > 0:
        emi = loan_amount / st.session_state.loan_term

    loan_ratio = 0

    if total_income > 0:
        loan_ratio = loan_amount / total_income

    payload = {

        "Gender_Male": 1 if st.session_state.gender == "Male" else 0,

        "Married_Yes":
            1 if st.session_state.marital_status == "Married" else 0,

        "Dependents":
            dependents,

        "Education_Not_Graduate":
            1 if st.session_state.education == "Not Graduate" else 0,

        "Self_Employed_Yes":
            1 if st.session_state.employment_status == "Yes" else 0,

        "ApplicantIncome":
            applicant_income,

        "CoapplicantIncome":
            coapplicant_income,

        "LoanAmount":
            loan_amount,

        "Loan_Amount_Term":
            st.session_state.loan_term,

        "Credit_History":
            1 if st.session_state.credit_history == "Yes" else 0,

        "Property_Area_Semiurban":
            1 if st.session_state.property_area == "Semiurban" else 0,

        "Property_Area_Urban":
            1 if st.session_state.property_area == "Urban" else 0,

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