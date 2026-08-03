import streamlit as st
from utils.validator import validate_income


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

        occupation = st.text_input(
            "Occupation *",
            value=st.session_state.get("occupation", ""),
            placeholder="Software Engineer",
        )
        st.session_state["occupation"] = occupation

        experience = st.number_input(
            "Years of Experience",
            min_value=0,
            max_value=50,
            value=st.session_state.get("experience", 0),
        )
        st.session_state["experience"] = experience

    with col2:

        applicant_income = st.number_input(
            "Applicant Monthly Income (₹) *",
            min_value=0.0,
            value=float(st.session_state.get("applicant_income", 0.0)),
        )
        st.session_state["applicant_income"] = applicant_income

        coapplicant_income = st.number_input(
            "Co-applicant Monthly Income (₹)",
            min_value=0.0,
            value=float(st.session_state.get("coapplicant_income", 0.0)),
        )
        st.session_state["coapplicant_income"] = coapplicant_income

        existing_emi = st.number_input(
            "Existing Monthly EMI (₹)",
            min_value=0.0,
            value=float(st.session_state.get("existing_emi", 0.0)),
        )
        st.session_state["existing_emi"] = existing_emi

    st.divider()

    if st.button(
        "Next ➜",
        key="income_next",
        use_container_width=True,
    ):

        errors = validate_income()

        if errors:
            for error in errors:
                st.error(error)
        else:
            st.session_state.step = 4
            st.rerun()