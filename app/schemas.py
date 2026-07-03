from pydantic import BaseModel


class LoanApplication(BaseModel):
    Gender_Male: int
    Married_Yes: int
    Dependents: int
    Education_Not_Graduate: int
    Self_Employed_Yes: int

    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float

    Property_Area_Semiurban: int
    Property_Area_Urban: int

    TotalIncome: float
    LogIncome: float
    LogLoanAmount: float
    EMI: float
    LoanToIncomeRatio: float
    IncomePerDependent: float