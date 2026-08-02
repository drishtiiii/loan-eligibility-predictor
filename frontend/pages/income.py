import streamlit as st


def show_income():

    st.subheader("💼 Step 3 of 7")

    st.title("Employment & Income")

    st.caption(
        "Provide your employment details and monthly income information."
    )

    st.divider()

    st.markdown("### 💼 Employment Details")

    col1, col2 = st.columns(2)

    with col1:

        st.text_input(
            "Occupation *",
            key="occupation",
            placeholder="Software Engineer",
        )

        st.number_input(
            "Years of Experience",
            min_value=0,
            max_value=50,
            key="experience",
        )

    with col2:

        st.number_input(
            "Applicant Monthly Income (₹) *",
            min_value=0.0,
            key="applicant_income",
        )

        st.number_input(
            "Co-applicant Monthly Income (₹)",
            min_value=0.0,
            key="coapplicant_income",
        )

        st.number_input(
            "Existing Monthly EMI (₹)",
            min_value=0.0,
            key="existing_emi",
        )