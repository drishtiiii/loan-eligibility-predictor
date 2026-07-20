import pandas as pd


def preprocess(data: dict):
    df = pd.DataFrame([data])
    return df