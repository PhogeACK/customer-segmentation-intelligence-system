import joblib
import pandas as pd

from src.config import (
    KMEANS_MODEL_PATH,
    SCALER_PATH
)

from src.preprocess import preprocess_data
from src.feature_engineering import engineer_features
from src.encoding import encode_features
from src.transform import transform_data
from src.business_intelligence import generate_business_intelligence


# -----------------------------------
# Load trained artifacts
# -----------------------------------

loaded_model = joblib.load(KMEANS_MODEL_PATH)

if isinstance(loaded_model, tuple):
    model = loaded_model[0]
else:
    model = loaded_model

loaded_scaler = joblib.load(SCALER_PATH)

if isinstance(loaded_scaler, tuple):
    scaler = loaded_scaler[0]
else:
    scaler = loaded_scaler


# -----------------------------------
# Batch prediction
# -----------------------------------

def predict_batch(df):

    # -----------------------------
    # Run preprocessing pipeline
    # -----------------------------

    df = preprocess_data(df)
    df = engineer_features(df)
    df = encode_features(df)

    # -----------------------------
    # Transform data
    # -----------------------------

    transformed = transform_data(
        df,
        scaler=scaler
    )

    if isinstance(transformed, tuple):
        df_scaled = transformed[0]
    else:
        df_scaled = transformed

    # -----------------------------
    # Predict clusters
    # -----------------------------

    cluster_predictions = model.predict(df_scaled)

    # -----------------------------
    # Create results dataframe
    # -----------------------------

    results_df = df.copy()

    results_df["cluster_id"] = cluster_predictions

    # -----------------------------
    # Generate Business Intelligence
    # -----------------------------

    business_df = pd.json_normalize(
        results_df["cluster_id"].apply(
            generate_business_intelligence
        )
    )

    # -----------------------------
    # Merge results
    # -----------------------------

    results_df = pd.concat(
        [results_df, business_df],
        axis=1
    )

    return results_df