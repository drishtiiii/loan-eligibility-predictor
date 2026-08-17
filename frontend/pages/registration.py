import streamlit as st
from datetime import date

from utils.validator import validate_registration


def show_registration():

    st.subheader("📝 Step 1 of 7")
    st.title("Applicant Registration")
    st.caption(
        "Please provide your basic personal information to begin your loan application."
    )

    st.divider()

    # ==========================================================
    # Personal Information
    # ==========================================================

    st.markdown("### 👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Full Name *",
            value=st.session_state.get("full_name", ""),
            placeholder="Enter your full name",
        )
        st.session_state["full_name"] = name

        st.selectbox(
            "Gender *",
            [
                "Select",
                "Male",
                "Female",
            ],
            key="gender",
        )

    with col2:

        today = date.today()

        dob = st.date_input(
            "Date of Birth *",
            min_value=date(1950, 1, 1),
            max_value=today,
            key="dob",
        )

        if dob:

            age = (
                today.year
                - dob.year
                - ((today.month, today.day) < (dob.month, dob.day))
            )

            st.session_state["age"] = age

            st.metric(
                "Calculated Age",
                f"{age} Years",
            )

    st.divider()

    # ==========================================================
    # Contact Information
    # ==========================================================

    st.markdown("### 📞 Contact Information")

    col1, col2 = st.columns(2)

    with col1:

        phone = st.text_input(
            "Phone Number *",
            value=st.session_state.get("phone", ""),
            placeholder="10-digit mobile number",
        )

        st.session_state["phone"] = phone

    with col2:

        email = st.text_input(
            "Email Address *",
            value=st.session_state.get("email", ""),
            placeholder="example@email.com",
        )

        st.session_state["email"] = email

    st.divider()

    # ==========================================================
    # Residential Address
    # ==========================================================

    st.markdown("### 🏠 Residential Address")

    address = st.text_area(
        "Street Address *",
        value=st.session_state.get("address", ""),
        placeholder="House No., Street, Locality",
        height=100,
    )

    st.session_state["address"] = address

    col1, col2 = st.columns(2)

    with col1:

        city = st.text_input(
            "City *",
            value=st.session_state.get("city", ""),
        )

        st.session_state["city"] = city

        state = st.text_input(
            "State *",
            value=st.session_state.get("state", ""),
        )

        st.session_state["state"] = state

    with col2:

        pin = st.text_input(
            "PIN Code *",
            value=st.session_state.get("pin_code", ""),
            max_chars=6,
        )

        st.session_state["pin_code"] = pin

        st.selectbox(
            "Country",
            ["India"],
            key="country",
        )

    st.divider()

    # ==========================================================
    # Next Button
    # ==========================================================

    if st.button(
        "Next ➜",
        key="registration_next",
        use_container_width=True,
    ):

        errors = validate_registration()

        if errors:

            for error in errors:
                st.error(error)

        else:

            st.session_state.step = 2
            st.rerun()