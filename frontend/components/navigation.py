import streamlit as st

from utils.validator import (
    validate_registration,
    validate_personal,
    validate_income,
    validate_loan,
    validate_credit,
)

TOTAL_STEPS = 7


def validate_current_step():

    step = st.session_state.step

    if step == 1:
        return validate_registration()

    elif step == 2:
        return validate_personal()

    elif step == 3:
        return validate_income()

    elif step == 4:
        return validate_loan()

    elif step == 5:
        return validate_credit()

    return []


def show_navigation():

    col1, col2, col3 = st.columns(3)

    # ---------------- BACK ----------------

    with col1:

        if st.session_state.step > 1:

            if st.button("⬅ Back", use_container_width=True):

                st.session_state.step -= 1
                st.rerun()

    # ---------------- RESET ----------------

    with col2:

        if st.button("🔄 Reset", use_container_width=True):

            for key in list(st.session_state.keys()):
                del st.session_state[key]

            st.rerun()

    # ---------------- NEXT ----------------

  #      with col3:

   #         if st.session_state.step < TOTAL_STEPS:

    #            if st.button("Next ➜", use_container_width=True):

     #               errors = validate_current_step()

      #              if errors:

       #                 for error in errors:
        #                    st.error(error)

         #           else:

          #              st.session_state.step += 1
           #             st.rerun()