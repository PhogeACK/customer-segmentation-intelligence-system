import numpy as np
import pandas as pd


def engineer_features(df):

    # ---------------------------------
    # Total customer spending
    # ---------------------------------
    spending_cols = [
        "MntWines",
        "MntFruits",
        "MntMeatProducts",
        "MntFishProducts",
        "MntSweetProducts",
        "MntGoldProds"
    ]

    df["total_spending"] = df[spending_cols].sum(axis=1)

    # ---------------------------------
    # Total purchase activity
    # ---------------------------------
    purchase_cols = [
        "NumStorePurchases",
        "NumWebPurchases"
    ]

    df["total_purchases"] = df[purchase_cols].sum(axis=1)

    # ---------------------------------
    # Web-dominant customers
    # ---------------------------------
    df["is_web_dominant"] = (
        (df["total_purchases"] > 0) &
        (
            df["NumWebPurchases"] /
            df["total_purchases"]
            > 0.5
        )
    ).astype(int)

    # ---------------------------------
    # Value optimizer customers
    # ---------------------------------
    df["value_optimizer"] = (
        (df["total_spending"] > df["total_spending"].median()) &
        (
            df["NumDealsPurchases"] /
            df["total_purchases"].replace(0, np.nan)
            > 0.6
        )
    ).astype(int)

    # ---------------------------------
    # Spending intensity
    # ---------------------------------
    df["spending_to_income_ratio"] = (
        df["total_spending"] / df["Income"]
    )

    # ---------------------------------
    # Family load
    # ---------------------------------
    df["total_dependents"] = (
        df["Kidhome"] + df["Teenhome"]
    )

    df["family_load"] = pd.cut(
        df["total_dependents"],
        bins=[-1, 0, 2, np.inf],
        labels=[0, 1, 2]
    ).astype(int)

    df.drop(columns=["total_dependents"], inplace=True)

    # ---------------------------------
    # Long tenure customers
    # ---------------------------------
    df["is_long_tenure"] = (
        df["tenure_years"] >
        df["tenure_years"].median()
    ).astype(int)

    return df