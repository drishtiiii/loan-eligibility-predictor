import streamlit as st
from utils.validator import validate_loan


def loan():

    st.subheader("🏦 Step 4 of 7")

    st.title("Loan Details")

    st.caption(
        "Tell us about the loan you are applying for."
    )

    st.divider()

    st.markdown("### 💰 Loan Information")

    col1, col2 = st.columns(2)

    with col1:

        loan_amount = st.number_input(
            "Requested Loan Amount (₹) *",
            min_value=0.0,
            value=float(st.session_state.get("loan_amount", 0.0)),
        )
        st.session_state["loan_amount"] = loan_amount

        loan_terms = [
            12,
            24,
            36,
            60,
            120,
            180,
            240,
            300,
            360,
        ]

        loan_term = st.selectbox(
            "Loan Term (Months) *",
            loan_terms,
            index=loan_terms.index(
                st.session_state.get("loan_term", 360)
            ),
        )

        st.session_state["loan_term"] = loan_term

    with col2:

        purpose_options = [
            "Home Loan",
            "Personal Loan",
            "Vehicle Loan",
            "Education Loan",
            "Business Loan",
            "Other",
        ]

        loan_purpose = st.selectbox(
            "Purpose of Loan",
            purpose_options,
            index=purpose_options.index(
                st.session_state.get(
                    "loan_purpose",
                    "Home Loan",
                )
            ),
        )

        st.session_state["loan_purpose"] = loan_purpose

        property_options = [
            "Select",
            "Urban",
            "Semiurban",
            "Rural",
        ]

        property_value = st.session_state.get("property_area", "Select")

        if property_value not in property_options:
            property_value = "Select"

        property_area = st.selectbox(
            "Property Area *",
            property_options,
            index=property_options.index(property_value),
        )

        st.session_state["property_area"] = property_area

        st.session_state["property_area"] = property_area

    st.divider()

    if st.button(
        "Next ➜",
        key="loan_next",
        use_container_width=True,
    ):

        errors = validate_loan()

        if errors:

            for error in errors:
                st.error(error)

        else:

            st.session_state.step = 5
            st.rerun()