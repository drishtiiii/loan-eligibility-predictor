import streamlit as st


def initialize_state():

    defaults = {

        # navigation
        "step": 1,

        # Registration
        "full_name": "",
        "age": None,
        "gender": "Select",
        "dob": None,
        "phone": "",
        "email": "",
        "address": "",
        "city": "",
        "state": "",
        "pin_code": "",
        "country": "India",

        # Personal
        "marital_status": "Select",
        "education": "Select",
        "employment_status": "No",
        "dependents": 0,

        # Income
        "applicant_income": 0.0,
        "coapplicant_income": 0.0,
        "occupation": "",
        "experience": 0,
        "existing_emi": 0.0,

        # Loan
        "loan_amount": 0.0,
        "loan_term": 360,
        "property_area": "Select",
        "loan_purpose": "Home Loan",

        # Credit
        "credit_history": "Yes",
        "previous_loan": "No",
        "loan_type": "Home Loan",
        "loan_status": "Paid",
        "credit_score": 750,
        "credit_declaration": False,

        # Prediction
        "prediction": None,
        "probability": None


    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value