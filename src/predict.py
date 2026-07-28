import pandas as pd
import joblib

from src.config import (
    KMEANS_MODEL_PATH,
    SCALER_PATH
)

from src.preprocess import preprocess_data
from src.feature_engineering import engineer_features
from src.encoding import encode_features
from src.transform import transform_data
from src.business_intelligence import generate_business_intelligence


# --------------------------------------------------
# Load trained artifacts
# --------------------------------------------------

kmeans_model = joblib.load(KMEANS_MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Safety check
if isinstance(kmeans_model, tuple):
    print("WARNING: Loaded model is a tuple. Using first element.")
    kmeans_model = kmeans_model[0]

print("Loaded model type:", type(kmeans_model))


# --------------------------------------------------
# Single customer prediction
# --------------------------------------------------

def predict_customer_segment(df):

    # ---------------------------------
    # Data preprocessing pipeline
    # ---------------------------------

    df = preprocess_data(df)
    df = engineer_features(df)
    df = encode_features(df)

    df_scaled, _ = transform_data(
        df=df,
        scaler=scaler,
        fit=False
    )

    # ---------------------------------
    # Predict customer cluster
    # ---------------------------------

    cluster_prediction = kmeans_model.predict(df_scaled)

    cluster_id = int(cluster_prediction[0])

    # ---------------------------------
    # Generate business intelligence
    # ---------------------------------

    business = generate_business_intelligence(cluster_id)

    # ---------------------------------
    # Build response
    # ---------------------------------

    result = {
        "cluster_id": cluster_id,
        **business
    }

    return result

def predict_batch(df):

    # -----------------------------
    # Data pipeline
    # -----------------------------

    df = preprocess_data(df)
    df = engineer_features(df)
    df = encode_features(df)

    df_scaled, _ = transform_data(
        df,
        scaler=scaler,
        fit=False
    )

    # -----------------------------
    # Predict all customers
    # -----------------------------

    cluster_ids = kmeans_model.predict(df_scaled)

    # -----------------------------
    # Build output
    # -----------------------------

    results = df.copy()

    results["cluster_id"] = cluster_ids

    business_rows = []

    for cluster_id in cluster_ids:

        business_rows.append(
            generate_business_intelligence(int(cluster_id))
        )

    business_df = pd.DataFrame(business_rows)

    results = pd.concat(
        [
            results.reset_index(drop=True),
            business_df.reset_index(drop=True)
        ],
        axis=1
    )

    return results