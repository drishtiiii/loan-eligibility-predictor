import streamlit as st

from utils.state import initialize_state
from pages.registration import show_registration
from components.navigation import show_navigation
from pages.personal import show_personal
from pages.income import show_income
from pages.loan import loan
from pages.credit import show_credit
from pages.review import show_review
from pages.result import show_result

from pathlib import Path
from components.header import show_header
from components.progress import show_progress


st.set_page_config(
    page_title="Loan Eligibility Portal",
    page_icon="🏦",
    layout="wide"
)

css = Path("frontend/assets/style.css").read_text()

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True,
)
initialize_state()
st.write(st.session_state)
show_header()
show_progress()


if st.session_state.step == 1:
    show_registration()

elif st.session_state.step == 2:
    show_personal()

elif st.session_state.step == 3:
    show_income()

elif st.session_state.step == 4:
    loan()

elif st.session_state.step == 5:
    show_credit()

elif st.session_state.step == 6:
    show_review()

elif st.session_state.step == 7:
    show_result()

st.divider()

show_navigation()