import streamlit as st


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

        st.number_input(
            "Requested Loan Amount (₹) *",
            min_value=0.0,
            key="loan_amount",
        )

        st.selectbox(
            "Loan Term (Months) *",
            [
                12,
                24,
                36,
                60,
                120,
                180,
                240,
                300,
                360,
            ],
            key="loan_term",
        )

    with col2:

        st.selectbox(
            "Purpose of Loan",
            [
                "Home Loan",
                "Personal Loan",
                "Vehicle Loan",
                "Education Loan",
                "Business Loan",
                "Other",
            ],
            key="loan_purpose",
        )

        st.selectbox(
            "Property Area *",
            [
                "Select",
                "Urban",
                "Semiurban",
                "Rural",
            ],
            key="property_area",
        )