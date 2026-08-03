import pandas as pd


FEATURE_ORDER = [
    "Dependents",
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History",
    "TotalIncome",
    "LogIncome",
    "LogLoanAmount",
    "EMI",
    "LoanToIncomeRatio",
    "IncomePerDependent",
    "Gender_Male",
    "Married_Yes",
    "Education_Not_Graduate",
    "Self_Employed_Yes",
    "Property_Area_Semiurban",
    "Property_Area_Urban",
]


def preprocess(data: dict):

    df = pd.DataFrame([data])

    df = df.rename(
        columns={
            "Education_Not_Graduate": "Education_Not Graduate"
        }
    )

    feature_order = [
        "Dependents",
        "ApplicantIncome",
        "CoapplicantIncome",
        "LoanAmount",
        "Loan_Amount_Term",
        "Credit_History",
        "TotalIncome",
        "LogIncome",
        "LogLoanAmount",
        "EMI",
        "LoanToIncomeRatio",
        "IncomePerDependent",
        "Gender_Male",
        "Married_Yes",
        "Education_Not Graduate",
        "Self_Employed_Yes",
        "Property_Area_Semiurban",
        "Property_Area_Urban",
    ]

    df = df[feature_order]

    return df