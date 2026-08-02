import requests

API_URL = "http://127.0.0.1:8000/predict"


def predict(payload):

    response = requests.post(
        API_URL,
        json=payload,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()