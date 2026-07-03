import numpy as np
import pandas as pd
import joblib

from app.config import FEATURE_COLUMNS_PATH

feature_columns = joblib.load(FEATURE_COLUMNS_PATH)


def preprocess(data: dict):
    df = pd.DataFrame([data])

    # Feature Engineering
    df["TotalIncome"] = (
        df["ApplicantIncome"] +
        df["CoapplicantIncome"]
    )

    df["LogIncome"] = np.log1p(df["TotalIncome"])

    df["LogLoanAmount"] = np.log1p(df["LoanAmount"])

    df["EMI"] = (
        df["LoanAmount"] /
        df["Loan_Amount_Term"]
    )

    df["LoanToIncomeRatio"] = (
        df["LoanAmount"] /
        df["TotalIncome"]
    )

    df["IncomePerDependent"] = (
        df["TotalIncome"] /
        (df["Dependents"] + 1)
    )

    # One-hot encode categorical columns
    df = pd.get_dummies(df)

    # Add any missing columns
    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0

    # Keep columns in the same order as training
    df = df[feature_columns]

    return df