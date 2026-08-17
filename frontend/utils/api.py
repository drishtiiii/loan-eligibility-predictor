import requests
import streamlit as st

API_URL = "https://loan-eligibility-predictor-ksgq.onrender.com/predict"

def predict(payload):

    response = requests.post(
        API_URL,
        json=payload,
        timeout=120,
    )

    st.write("Payload Sent:")
    st.json(payload)

    st.write("Status Code:", response.status_code)

    try:
        st.json(response.json())
    except Exception:
        st.write(response.text)

    response.raise_for_status()

    return response.json()