import streamlit as st

from utils.validator import (
    validate_registration,
    validate_personal,
    validate_income,
    validate_loan,
    validate_credit,
)

TOTAL_STEPS = 7


def next_step():
    if st.session_state.step < TOTAL_STEPS:
        st.session_state.step += 1


def previous_step():
    if st.session_state.step > 1:
        st.session_state.step -= 1


def reset_application():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

    st.rerun()


def show_navigation():

    col1, col2, col3 = st.columns([1, 1, 1])

    # ---------------- BACK ----------------

    with col1:

        if st.session_state.step > 1:

            if st.button("⬅ Back", use_container_width=True):
                previous_step()
                st.rerun()

    # ---------------- RESET ----------------

    with col2:

        if st.button("🔄 Reset", use_container_width=True):
            reset_application()

    # ---------------- NEXT ----------------

    with col3:

        button_text = "Next ➜"

        if st.session_state.step < TOTAL_STEPS:

            if st.button(button_text, use_container_width=True):

                errors = []

                if st.session_state.step == 1:
                    errors = validate_registration()

                elif st.session_state.step == 2:
                    errors = validate_personal()

                elif st.session_state.step == 3:
                    errors = validate_income()

                elif st.session_state.step == 4:
                    errors = validate_loan()

                elif st.session_state.step == 5:
                    errors = validate_credit()

                elif st.session_state.step == 6:
                    # API call will go here next
                    return

                if errors:

                    for error in errors:
                        st.error(error)

                else:
                    next_step()
                    st.rerun()