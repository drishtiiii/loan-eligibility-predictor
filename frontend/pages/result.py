import streamlit as st
from datetime import datetime


def show_result():

    approved = st.session_state.get("prediction", False)
    probability = st.session_state.get("probability", 0)

    application_id = datetime.now().strftime("APP-%Y%m%d-%H%M%S")

    st.subheader("🎯 Application Result")

    st.title("Loan Eligibility Prediction")

    st.divider()

    st.metric(
        "Application ID",
        application_id,
    )

    st.divider()

    if approved:

        st.success("🎉 Congratulations! Your loan is likely to be Approved.")

    else:

        st.error("❌ Your loan is likely to be Rejected.")

    st.metric(
        "Approval Probability",
        f"{probability:.2f}%"
    )

    st.divider()

    st.subheader("Summary")

    st.write(f"**Applicant:** {st.session_state.full_name}")

    st.write(f"**Loan Amount:** ₹ {st.session_state.loan_amount:,.2f}")

    st.write(f"**Monthly Income:** ₹ {st.session_state.applicant_income:,.2f}")

    st.write(f"**Credit History:** {st.session_state.credit_history}")

    st.divider()

    if approved:

        st.info(
            """
Your application satisfies the model's eligibility criteria.

The final approval remains subject to document verification
and lender policies.
"""
        )

    else:

        st.warning(
            """
The model predicts a low chance of approval.

You may improve your chances by:

• Increasing income

• Applying for a smaller loan

• Improving credit history

• Adding a co-applicant
"""
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🏠 New Application",
            use_container_width=True,
        ):

            for key in list(st.session_state.keys()):
                del st.session_state[key]

            st.rerun()

    with col2:

        st.download_button(
            "📄 Download Result",
            data=f"""
Application ID : {application_id}

Prediction : {"Approved" if approved else "Rejected"}

Probability : {probability:.2f}%
""",
            file_name="loan_prediction.txt",
            use_container_width=True,
        )