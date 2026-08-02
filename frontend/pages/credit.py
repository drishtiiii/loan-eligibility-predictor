import streamlit as st


def show_credit():

    st.subheader("💳 Step 5 of 7")

    st.title("Credit Assessment")

    st.caption(
        "Provide information regarding your previous loans and credit history."
    )

    st.divider()

    st.markdown("### Previous Loan Details")

    st.radio(
        "Have you previously taken a loan? *",
        ["Yes", "No"],
        key="previous_loan",
        horizontal=True,
    )

    if st.session_state.previous_loan == "Yes":

        col1, col2 = st.columns(2)

        with col1:

            st.selectbox(
                "Loan Type",
                [
                    "Home Loan",
                    "Vehicle Loan",
                    "Education Loan",
                    "Personal Loan",
                    "Business Loan",
                    "Other",
                ],
                key="loan_type",
            )

        with col2:

            st.selectbox(
                "Loan Status",
                [
                    "Fully Repaid",
                    "Ongoing",
                    "Defaulted",
                ],
                key="loan_status",
            )

    st.divider()

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
        value=750,
        key="credit_score",
        help="This field is not used by the current prediction model.",
    )

    st.checkbox(
        "I confirm that the information provided above is true.",
        key="credit_declaration",
    )