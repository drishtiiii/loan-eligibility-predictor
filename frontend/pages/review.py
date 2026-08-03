import streamlit as st
from utils.mapper import build_payload
from utils.api import predict


def show_review():

    st.subheader("📋 Step 6 of 7")

    st.title("Review Your Application")

    st.caption(
        "Please verify your information before submitting your application."
    )

    st.divider()

    # -----------------------------------------------------
    # Personal Information
    # -----------------------------------------------------

    with st.expander("👤 Personal Information", expanded=True):

        col1, col2 = st.columns(2)

        with col1:

            st.write("**Full Name:**", st.session_state.get("full_name", ""))

            st.write("**Gender:**", st.session_state.get("gender", "Not Selected"))

            st.write("**Phone:**", st.session_state.get("phone", ""))

            st.write("**Email:**", st.session_state.get("email", ""))

        with col2:

            st.write("**City:**", st.session_state.get("city", ""))

            st.write("**State:**", st.session_state.get("state", ""))

            st.write("**PIN Code:**", st.session_state.get("pin_code", ""))

    # -----------------------------------------------------
    # Personal Details
    # -----------------------------------------------------

    with st.expander("👨‍👩‍👧 Family Details"):

        st.write("**Marital Status:**", st.session_state.get("marital_status", ""))

        st.write("**Dependents:**", st.session_state.get("dependents", 0))

        st.write("**Education:**", st.session_state.get("education", ""))

        st.write("**Self Employed:**", st.session_state.get("employment_status", ""))

    # -----------------------------------------------------
    # Income
    # -----------------------------------------------------

    with st.expander("💼 Employment & Income"):

        st.write("**Occupation:**", st.session_state.get("occupation", ""))

        st.write("**Experience:**", st.session_state.get("experience", 0), "Years")

        st.write("**Applicant Income:** ₹", st.session_state.get("applicant_income", 0))

        st.write("**Co-applicant Income:** ₹", st.session_state.get("coapplicant_income", 0))

        st.write("**Existing EMI:** ₹", st.session_state.get("existing_emi", 0))

    # -----------------------------------------------------
    # Loan
    # -----------------------------------------------------

    with st.expander("🏦 Loan Details"):

        st.write("**Loan Amount:** ₹", st.session_state.get("loan_amount", 0))

        st.write("**Loan Term:**", st.session_state.get("loan_term", 360), "Months")

        st.write("**Purpose:**", st.session_state.get("loan_purpose", ""))

        st.write("**Property Area:**", st.session_state.get("property_area", ""))

    # -----------------------------------------------------
    # Credit
    # -----------------------------------------------------

    with st.expander("💳 Credit Profile"):

        st.write("**Previous Loan:**", st.session_state.get("previous_loan", ""))

        st.write("**Credit History:**", st.session_state.get("credit_history", ""))

        st.write("**Credit Score:**", st.session_state.get("credit_score", ""))

    st.divider()

    # -----------------------------------------------------
    # Submit
    # -----------------------------------------------------

    if st.button(
        "🚀 Submit Application",
        key="submit_application",
        type="primary",
        use_container_width=True,
    ):

        with st.spinner("Analyzing your application..."):

            payload = build_payload()

            result = predict(payload)

            st.session_state["prediction"] = result["loan_approved"]

            st.session_state["probability"] = result["approval_probability"]

            st.session_state["step"] = 7

            st.rerun()