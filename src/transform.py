import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler


# ---------------------------------
# Feature transformation pipeline
# ---------------------------------
def transform_data(
    df,
    scaler=None,
    fit=True
):

    df = df.copy()

    # -----------------------------
    # Log transformations
    # -----------------------------
    log_features = [
        "Income",
        "MntWines",
        "MntFruits",
        "MntMeatProducts",
        "MntFishProducts",
        "MntGoldProds",
        "NumDealsPurchases",
        "NumCatalogPurchases",
        "NumWebPurchases"
    ]

    for col in log_features:
        df[f"{col}_log"] = np.log1p(df[col])

    # -----------------------------
    # Drop original columns
    # -----------------------------
    original_features_to_drop = [
        "Income",
        "MntWines",
        "MntFruits",
        "MntMeatProducts",
        "MntFishProducts",
        "MntGoldProds",
        "NumDealsPurchases",
        "NumCatalogPurchases",
        "NumWebPurchases"
    ]

    df = df.drop(columns=original_features_to_drop)

    # -----------------------------
    # Feature selection drops
    # -----------------------------
    features_to_drop = [
        "AcceptedCmp1",
        "Education_ord",
        "Response",
        "NumWebVisitsMonth",
        "MntSweetProducts"
    ]

    df = df.drop(columns=features_to_drop, errors="ignore")

    # -----------------------------
    # Scaling
    # -----------------------------
    if fit:

        scaler = StandardScaler()

        df_scaled = scaler.fit_transform(df)

    else:

        # ---------------------------------
        # Ensure feature order matches training
        # ---------------------------------
        if hasattr(scaler, "feature_names_in_"):
            df = df.reindex(columns=scaler.feature_names_in_)

        df_scaled = scaler.transform(df)

    # -----------------------------
    # Convert back to DataFrame
    # -----------------------------
    df_scaled = pd.DataFrame(
        df_scaled,
        columns=df.columns,
        index=df.index
    )

    return df_scaled, scaler