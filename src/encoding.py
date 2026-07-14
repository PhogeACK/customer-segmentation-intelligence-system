def encode_features(df):

    # -----------------------------
    # Education encoding
    # -----------------------------
    education_order = {
        "Basic": 0,
        "2n Cycle": 1,
        "Graduation": 2,
        "Master": 3,
        "PhD": 4
    }

    df["Education_ord"] = (
        df["Education"]
        .map(education_order)
    )

    df.drop(
        columns=["Education"],
        inplace=True
    )

    # -----------------------------
    # Marital Status encoding
    # -----------------------------
    df["Marital_Status_clean"] = (
        df["Marital_Status"]
        .replace(
            ["Alone", "Absurd", "YOLO"],
            "Other"
        )
    )

    marital_mapping = {
        "Married": 0,
        "Together": 1,
        "Single": 2,
        "Divorced": 3,
        "Widow": 4,
        "Other": 5
    }

    df["Marital_Status_encoded"] = (
        df["Marital_Status_clean"]
        .map(marital_mapping)
    )

    df.drop(
        columns=[
            "Marital_Status",
            "Marital_Status_clean"
        ],
        inplace=True
    )

    return df