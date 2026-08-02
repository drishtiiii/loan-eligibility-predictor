import streamlit as st

TOTAL_STEPS = 7

STEP_NAMES = [
    "Registration",
    "Personal",
    "Income",
    "Loan",
    "Credit",
    "Review",
    "Result",
]


def show_progress():

    step = st.session_state.step

    st.progress(step / TOTAL_STEPS)

    st.caption(f"Step {step} of {TOTAL_STEPS}")

    cols = st.columns(TOTAL_STEPS)

    for i, col in enumerate(cols):

        if i + 1 < step:
            col.success("✓")

        elif i + 1 == step:
            col.info(STEP_NAMES[i])

        else:
            col.write(STEP_NAMES[i])