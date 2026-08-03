import streamlit as st
from utils.validator import validate_credit


def show_credit():

    st.subheader("💳 Step 5 of 7")

    st.title("Credit Assessment")

    st.caption(
        "Provide information regarding your previous loans and credit history."
    )

    st.divider()

    st.markdown("### Previous Loan Details")

    previous_options = [
        "Yes",
        "No",
    ]

    previous_loan = st.radio(
        "Have you previously taken a loan? *",
        previous_options,
        index=previous_options.index(
            st.session_state.get("previous_loan", "No")
        ),
        horizontal=True,
    )

    st.session_state["previous_loan"] = previous_loan

    if previous_loan == "Yes":

        col1, col2 = st.columns(2)

        loan_type_options = [
            "Home Loan",
            "Vehicle Loan",
            "Education Loan",
            "Personal Loan",
            "Business Loan",
            "Other",
        ]

        loan_status_options = [
            "Fully Repaid",
            "Ongoing",
            "Defaulted",
        ]

        with col1:

            loan_type = st.selectbox(
                "Loan Type",
                loan_type_options,
                index=loan_type_options.index(
                    st.session_state.get(
                        "loan_type",
                        "Home Loan",
                    )
                ),
            )

            st.session_state["loan_type"] = loan_type

        with col2:

            loan_status = st.selectbox(
                "Loan Status",
                loan_status_options,
                index=loan_status_options.index(
                    st.session_state.get(
                        "loan_status",
                        "Fully Repaid",
                    )
                ),
            )

            st.session_state["loan_status"] = loan_status

    st.divider()

    st.markdown("### Credit History")

    credit_options = [
        "Yes",
        "No",
    ]

    credit_history = st.radio(
        "Do you have a good credit history? *",
        credit_options,
        index=credit_options.index(
            st.session_state.get("credit_history", "Yes")
        ),
        horizontal=True,
    )

    st.session_state["credit_history"] = credit_history

    credit_score = st.number_input(
        "Credit Score (Optional)",
        min_value=300,
        max_value=900,
        value=int(st.session_state.get("credit_score", 750)),
        help="This field is not used by the current prediction model.",
    )

    st.session_state["credit_score"] = credit_score

    declaration = st.checkbox(
        "I confirm that the information provided above is true.",
        value=st.session_state.get("credit_declaration", False),
    )

    st.session_state["credit_declaration"] = declaration

    st.divider()

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