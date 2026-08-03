import re
import streamlit as st


def validate_registration():

    errors = []

    if not st.session_state.full_name.strip():
        errors.append("Full Name is required.")

    if st.session_state.age is None or st.session_state.age < 18:
        errors.append("Applicant must be at least 18 years old.")

    if st.session_state.gender == "Select":
        errors.append("Please select your gender.")

    phone = st.session_state.phone.strip()

    if not re.fullmatch(r"\d{10}", phone):
        errors.append("Phone number must contain exactly 10 digits.")

    email = st.session_state.email.strip()

    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        errors.append("Please enter a valid email address.")

    if not st.session_state.address.strip():
        errors.append("Address is required.")

    if not st.session_state.city.strip():
        errors.append("City is required.")

    if not st.session_state.state.strip():
        errors.append("State is required.")

    pin = st.session_state.pin_code.strip()

    if not re.fullmatch(r"\d{6}", pin):
        errors.append("PIN Code must contain 6 digits.")

    return errors

def validate_personal():

    errors = []

    if st.session_state.marital_status == "Select":
        errors.append("Please select your marital status.")

    if st.session_state.education == "Select":
        errors.append("Please select your qualification.")

    if st.session_state.employment_status == "Select":
        errors.append("Please select your employment status.")

    return errors

def validate_income():

    errors = []

    if not st.session_state.occupation.strip():
        errors.append("Occupation is required.")

    if st.session_state.applicant_income <= 0:
        errors.append("Applicant income must be greater than zero.")

    if st.session_state.experience < 0:
        errors.append("Years of experience cannot be negative.")

    return errors

def validate_loan():

    errors = []

    if st.session_state.loan_amount <= 0:
        errors.append("Loan amount must be greater than zero.")

    if st.session_state.property_area == "Select":
        errors.append("Please select the property area.")

    return errors

def validate_credit():

    errors = []

    if not st.session_state.credit_declaration:
        errors.append("Please accept the declaration before continuing.")

    return errors