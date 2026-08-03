import streamlit as st


def show_personal():
    st.info(f"DEBUG Step 2: {st.session_state.full_name}")
    
    st.subheader("👨‍👩‍👧 Step 2 of 7")

    st.title("Personal Information")

    st.caption(
        "Tell us a little about your family and educational background."
    )

    st.divider()

    st.markdown("### 👨‍👩‍👧 Family Details")

    col1, col2 = st.columns(2)

    with col1:

        st.selectbox(
            "Marital Status *",
            [
                "Select",
                "Married",
                "Single",
            ],
            key="marital_status",
        )

        st.selectbox(
            "Number of Dependents *",
            [
                0,
                1,
                2,
                3,
            ],
            key="dependents",
        )

    with col2:

        st.selectbox(
            "Highest Qualification *",
            [
                "Select",
                "Graduate",
                "Post Graduate",
                "Not Graduate",
            ],
            key="education",
        )

        st.radio(
            "Are you Self Employed? *",
            [
                "Yes",
                "No",
            ],
            key="employment_status",
            horizontal=True,
        )