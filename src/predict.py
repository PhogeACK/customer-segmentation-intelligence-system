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


# ---------------------------------
# Load trained artifacts
# ---------------------------------

kmeans_model = joblib.load(KMEANS_MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


# ---------------------------------
# Single customer prediction
# ---------------------------------

def predict_customer_segment(df):

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
    # Predict cluster
    # -----------------------------

    cluster_id = int(
        kmeans_model.predict(df_scaled)[0]
    )

    # -----------------------------
    # Business Intelligence
    # -----------------------------

    business = generate_business_intelligence(cluster_id)

    # -----------------------------
    # Final Result
    # -----------------------------

    result = {
        "cluster_id": cluster_id,
        **business
    }

    return result