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
from src.persona_engine import enrich_cluster_output
from src.recommendation_engine import get_recommendation
from src.workflow_engine import get_workflow


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
# Batch prediction function
# -----------------------------------
def predict_batch(df):

    # -----------------------------
    # Run preprocessing pipeline
    # -----------------------------
    df = preprocess_data(df)
    df = engineer_features(df)
    df = encode_features(df)

    # -----------------------------
    # Apply transformations
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
    # Add cluster results
    # -----------------------------
    results_df = df.copy()

    results_df["cluster_id"] = cluster_predictions

    # -----------------------------
    # Persona information
    # -----------------------------
    results_df["segment_name"] = (
        results_df["cluster_id"]
        .apply(lambda x: enrich_cluster_output(x)["segment_name"])
    )

    results_df["behavior"] = (
        results_df["cluster_id"]
        .apply(lambda x: enrich_cluster_output(x)["behavior"])
    )

    results_df["business_value"] = (
        results_df["cluster_id"]
        .apply(lambda x: enrich_cluster_output(x)["business_value"])
    )

    results_df["recommended_action"] = (
        results_df["cluster_id"]
        .apply(lambda x: enrich_cluster_output(x)["recommended_action"])
    )

    # -----------------------------
    # Business recommendations
    # -----------------------------
    recommendation_data = (
        results_df["segment_name"]
        .apply(get_recommendation)
    )

    results_df["primary_goal"] = (
        recommendation_data
        .apply(lambda x: x["primary_goal"])
    )

    results_df["opportunity"] = (
        recommendation_data
        .apply(lambda x: x["opportunity"])
    )

    results_df["risk"] = (
        recommendation_data
        .apply(lambda x: x["risk"])
    )

    results_df["recommended_campaign"] = (
        recommendation_data
        .apply(lambda x: x["recommended_campaign"])
    )

        # -----------------------------
    # Workflow recommendations
    # -----------------------------
    workflow_data = (
        results_df["segment_name"]
        .apply(get_workflow)
    )

    results_df["workflow_name"] = (
        workflow_data
        .apply(lambda x: x["workflow_name"])
    )

    results_df["workflow_trigger"] = (
        workflow_data
        .apply(lambda x: x["workflow_trigger"])
    )

    results_df["priority"] = (
        workflow_data
        .apply(lambda x: x["priority"])
    )

    return results_df