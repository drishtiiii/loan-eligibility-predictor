import streamlit as st


def show_header():

    st.markdown(
        """
        <div class="section-title">
            🏦 Credit Loan Eligibility Platform
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="subtitle">
        AI-powered Loan Approval Recommendation System
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()