import streamlit as st
from utils.mapper import build_payload
from utils.api import predict

def show_review():

    st.write(st.session_state)
    
    st.subheader("📋 Step 6 of 7")

    st.title("Review Your Application")

    st.caption(
        "Please verify your information before submitting your application."
    )

    st.divider()

    with st.expander("👤 Personal Information", expanded=True):

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Full Name:**", st.session_state.full_name)
            st.write("**Age:**", st.session_state.age)
            st.write("**Gender:**", st.session_state.gender)
            st.write("**Phone:**", st.session_state.phone)

        with col2:
            st.write("**Email:**", st.session_state.email)
            st.write("**City:**", st.session_state.city)
            st.write("**State:**", st.session_state.state)
            st.write("**PIN Code:**", st.session_state.pin_code)

    with st.expander("👨‍👩‍👧 Family Details"):

        st.write("**Marital Status:**", st.session_state.marital_status)
        st.write("**Dependents:**", st.session_state.dependents)
        st.write("**Education:**", st.session_state.education)
        st.write("**Self Employed:**", st.session_state.employment_status)

    with st.expander("💼 Employment & Income"):

        st.write("**Occupation:**", st.session_state.occupation)
        st.write("**Experience:**", st.session_state.experience, "Years")
        st.write("**Applicant Income:** ₹", st.session_state.applicant_income)
        st.write("**Co-applicant Income:** ₹", st.session_state.coapplicant_income)
        st.write("**Existing EMI:** ₹", st.session_state.existing_emi)

    with st.expander("🏦 Loan Details"):

        st.write("**Loan Amount:** ₹", st.session_state.loan_amount)
        st.write("**Loan Term:**", st.session_state.loan_term, "Months")
        st.write("**Purpose:**", st.session_state.loan_purpose)
        st.write("**Property Area:**", st.session_state.property_area)

    with st.expander("💳 Credit Profile"):

        st.write("**Previous Loan:**", st.session_state.previous_loan)
        st.write("**Credit History:**", st.session_state.credit_history)

    if st.button(
    "🚀 Submit Application",
    type="primary",
    use_container_width=True,
):

        with st.spinner("Analyzing your application..."):

            payload = build_payload()

            result = predict(payload)

            st.session_state.prediction = result["loan_approved"]

            st.session_state.probability = result["approval_probability"]

            st.session_state.step = 7

            st.rerun()

