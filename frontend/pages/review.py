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

    # =====================================================
    # Personal Information
    # =====================================================

    with st.expander("👤 Personal Information", expanded=True):

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                "**Full Name:**",
                st.session_state.get("full_name", "Not provided")
            )

            gender = st.session_state.get("gender", "Select")

            if gender == "Select" or not gender:
                gender = "Not Selected"

            st.write("**Gender:**", gender)

            st.write(
                "**Phone:**",
                st.session_state.get("phone", "Not provided")
            )

            st.write(
                "**Email:**",
                st.session_state.get("email", "Not provided")
            )

        with col2:

            st.write(
                "**Date of Birth:**",
                st.session_state.get("dob", "Not provided")
            )

            st.write(
                "**Age:**",
                st.session_state.get("age", "Not provided")
            )

            st.write(
                "**City:**",
                st.session_state.get("city", "Not provided")
            )

            st.write(
                "**State:**",
                st.session_state.get("state", "Not provided")
            )

            st.write(
                "**PIN Code:**",
                st.session_state.get("pin_code", "Not provided")
            )

    # =====================================================
    # Family Details
    # =====================================================

    with st.expander("👨‍👩‍👧 Family Details"):

        st.write(
            "**Marital Status:**",
            st.session_state.get("marital_status", "Not provided")
        )

        st.write(
            "**Dependents:**",
            st.session_state.get("dependents", 0)
        )

        st.write(
            "**Education:**",
            st.session_state.get("education", "Not provided")
        )

        st.write(
            "**Self Employed:**",
            st.session_state.get("employment_status", "Not provided")
        )

    # =====================================================
    # Employment & Income
    # =====================================================

    with st.expander("💼 Employment & Income"):

        st.write(
            "**Occupation:**",
            st.session_state.get("occupation", "Not provided")
        )

        st.write(
            "**Experience:**",
            st.session_state.get("experience", 0),
            "Years"
        )

        st.write(
            "**Applicant Income:** ₹",
            st.session_state.get("applicant_income", 0)
        )

        st.write(
            "**Co-applicant Income:** ₹",
            st.session_state.get("coapplicant_income", 0)
        )

        st.write(
            "**Existing EMI:** ₹",
            st.session_state.get("existing_emi", 0)
        )

    # =====================================================
    # Loan Details
    # =====================================================

    with st.expander("🏦 Loan Details"):

        st.write(
            "**Loan Amount:** ₹",
            st.session_state.get("loan_amount", 0)
        )

        st.write(
            "**Loan Term:**",
            st.session_state.get("loan_term", 360),
            "Months"
        )

        st.write(
            "**Purpose:**",
            st.session_state.get("loan_purpose", "Not provided")
        )

        st.write(
            "**Property Area:**",
            st.session_state.get("property_area", "Not provided")
        )

    # =====================================================
    # Credit Profile
    # =====================================================

    with st.expander("💳 Credit Profile"):

        st.write(
            "**Previous Loan:**",
            st.session_state.get("previous_loan", "Not provided")
        )

        st.write(
            "**Credit History:**",
            st.session_state.get("credit_history", "Not provided")
        )

        st.write(
            "**Credit Score:**",
            st.session_state.get("credit_score", "Not provided")
        )

    st.divider()

    # =====================================================
    # Submit Application
    # =====================================================

    if st.button(
        "🚀 Submit Application",
        key="submit_application",
        type="primary",
        use_container_width=True,
    ):

        with st.spinner("Analyzing your application..."):

            try:

                # Build ML payload
                payload = build_payload()

                # Send payload to FastAPI
                result = predict(payload)

                # Store prediction
                st.session_state["prediction"] = result["loan_approved"]

                st.session_state["probability"] = result[
                    "approval_probability"
                ]

                # Move to result page
                st.session_state["step"] = 7

                st.rerun()

            except Exception as e:

                st.error(
                    "Unable to process the application. "
                    "Please try again."
                )

                st.exception(e)