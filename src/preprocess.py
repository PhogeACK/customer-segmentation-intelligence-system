import pandas as pd


def preprocess_data(df):

    # -----------------------------
    # Drop irrelevant columns
    # -----------------------------
    df = df.drop(
        columns=["ID", "Z_Revenue", "Z_CostContact"],
        errors="ignore"
    )

    # -----------------------------
    # Handle missing income values
    # -----------------------------
    income_median = df["Income"].median()
    df["Income"] = df["Income"].fillna(income_median)

    # -----------------------------
    # Convert customer date
    # into tenure feature
    # -----------------------------
    df["Dt_Customer"] = pd.to_datetime(
    df["Dt_Customer"],
    format="mixed",
    dayfirst=True

    )

    reference_date = df["Dt_Customer"].max()

    df["tenure_years"] = (
        (reference_date - df["Dt_Customer"]).dt.days / 365.25
    ).round(3)

    # Drop original date column
    df = df.drop(columns=["Dt_Customer"])

    return df