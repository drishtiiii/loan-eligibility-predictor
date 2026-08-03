import streamlit as st
from pathlib import Path

from utils.state import initialize_state

from components.header import show_header
from components.progress import show_progress
from components.navigation import show_navigation

from pages.registration import show_registration
from pages.personal import show_personal
from pages.income import show_income
from pages.loan import loan
from pages.credit import show_credit
from pages.review import show_review
from pages.result import show_result



st.set_page_config(
    page_title="Loan Eligibility Portal",
    page_icon="🏦",
    layout="wide",
)

import sys
st.sidebar.write("Python:", sys.executable)

css = Path("frontend/assets/style.css").read_text()

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True,
)
if "step" not in st.session_state:
    initialize_state()

show_header()

show_progress()

PAGES = {
    1: show_registration,
    2: show_personal,
    3: show_income,
    4: loan,
    5: show_credit,
    6: show_review,
    7: show_result,
}

st.sidebar.write("### APP SESSION")
st.sidebar.write(st.session_state.get("full_name"))
st.sidebar.write(st.session_state.get("step"))


PAGES[st.session_state.step]()

st.divider()

show_navigation()