import streamlit as st
from datetime import date


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

        st.text_input(
            "Full Name *",
            key="full_name",
            placeholder="Enter your full name",
        )
        st.success(f"DEBUG: {st.session_state.full_name}")
        
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
            value=st.session_state.get("dob") or date(2000, 1, 1),
            min_value=date(1950, 1, 1),
            max_value=today,
            key="dob",
        )

        if dob is not None:
            age = (
                today.year
                - dob.year
                - ((today.month, today.day) < (dob.month, dob.day))
            )

            st.session_state.age = age

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

        st.text_input(
            "Phone Number *",
            key="phone",
            placeholder="10-digit mobile number",
        )

    with col2:

        st.text_input(
            "Email Address *",
            key="email",
            placeholder="example@email.com",
        )

    st.divider()

    # ==========================================================
    # Residential Address
    # ==========================================================

    st.markdown("### 🏠 Residential Address")

    st.text_area(
        "Street Address *",
        key="address",
        height=100,
        placeholder="House No., Street, Locality",
    )

    col1, col2 = st.columns(2)

    with col1:

        st.text_input(
            "City *",
            key="city",
        )

        st.text_input(
            "State *",
            key="state",
        )

    with col2:

        st.text_input(
            "PIN Code *",
            key="pin_code",
            max_chars=6,
        )

        st.selectbox(
            "Country",
            ["India"],
            key="country",
        )