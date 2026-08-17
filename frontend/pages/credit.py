import streamlit as st
from utils.validator import validate_credit


def show_credit():

    st.subheader("💳 Step 5 of 7")

    st.title("Credit Assessment")

    st.caption(
        "Provide information regarding your previous loans and credit history."
    )

    st.divider()

    # =====================================================
    # Previous Loan Details
    # =====================================================

    st.markdown("### Previous Loan Details")

    st.radio(
        "Have you previously taken a loan? *",
        ["Yes", "No"],
        key="previous_loan",
        horizontal=True,
    )

    if st.session_state.get("previous_loan") == "Yes":

        col1, col2 = st.columns(2)

        with col1:

            loan_type_options = [
                "Home Loan",
                "Vehicle Loan",
                "Education Loan",
                "Personal Loan",
                "Business Loan",
                "Other",
            ]

            current_loan_type = st.session_state.get(
                "loan_type",
                "Home Loan"
            )

            if current_loan_type not in loan_type_options:
                current_loan_type = "Home Loan"

            st.selectbox(
                "Loan Type",
                loan_type_options,
                index=loan_type_options.index(current_loan_type),
                key="loan_type",
            )

        with col2:

            loan_status_options = [
                "Fully Repaid",
                "Ongoing",
                "Defaulted",
            ]

            current_loan_status = st.session_state.get(
                "loan_status",
                "Fully Repaid"
            )

            if current_loan_status not in loan_status_options:
                current_loan_status = "Fully Repaid"

            st.selectbox(
                "Loan Status",
                loan_status_options,
                index=loan_status_options.index(current_loan_status),
                key="loan_status",
            )

    st.divider()

    # =====================================================
    # Credit History
    # =====================================================

    st.markdown("### Credit History")

    st.radio(
        "Do you have a good credit history? *",
        ["Yes", "No"],
        key="credit_history",
        horizontal=True,
    )

    st.number_input(
        "Credit Score (Optional)",
        min_value=300,
        max_value=900,
        key="credit_score",
        help="This field is not used by the current prediction model.",
    )

    st.checkbox(
        "I confirm that the information provided above is true.",
        key="credit_declaration",
    )

    st.divider()

    # =====================================================
    # Next
    # =====================================================

    if st.button(
        "Next ➜",
        key="credit_next",
        use_container_width=True,
    ):

        errors = validate_credit()

        if errors:

            for error in errors:
                st.error(error)

        else:

            st.session_state.step = 6
            st.rerun()

   