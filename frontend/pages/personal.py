import streamlit as st
from utils.validator import validate_personal


def show_personal():

    st.subheader("👨‍👩‍👧 Step 2 of 7")
    st.title("Personal Information")

    st.caption(
        "Tell us a little about your family and educational background."
    )

    st.divider()

    st.markdown("### 👨‍👩‍👧 Family Details")

    col1, col2 = st.columns(2)

    # ---------------- Marital Status ----------------

    marital_options = [
        "Select",
        "Married",
        "Single",
    ]

    # ---------------- Dependents ----------------

    dependent_options = [0, 1, 2, 3]

    # ---------------- Education ----------------

    education_options = [
        "Select",
        "Graduate",
        "Post Graduate",
        "Not Graduate",
    ]

    # ---------------- Employment ----------------

    employment_options = [
        "Yes",
        "No",
    ]

    with col1:

        marital_status = st.selectbox(
            "Marital Status *",
            marital_options,
            index=marital_options.index(
                st.session_state.get("marital_status", "Select")
            ),
        )

        st.session_state["marital_status"] = marital_status

        dependents = st.selectbox(
            "Number of Dependents *",
            dependent_options,
            index=dependent_options.index(
                st.session_state.get("dependents", 0)
            ),
        )

        st.session_state["dependents"] = dependents

    with col2:

        education = st.selectbox(
            "Highest Qualification *",
            education_options,
            index=education_options.index(
                st.session_state.get("education", "Select")
            ),
        )

        st.session_state["education"] = education

        employment_value = st.session_state.get("employment_status", "No")

        if employment_value not in employment_options:
            employment_value = "No"

        employment = st.radio(
            "Are you Self Employed? *",
            employment_options,
            index=employment_options.index(employment_value),
            horizontal=True,
        )
        
        st.session_state["employment_status"] = employment

    st.divider()

    if st.button(
        "Next ➜",
        key="personal_next",
        use_container_width=True,
    ):

        errors = validate_personal()

        if errors:

            for error in errors:
                st.error(error)

        else:

            st.session_state.step = 3
            st.rerun()