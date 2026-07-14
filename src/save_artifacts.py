import joblib

from src.config import (
    KMEANS_MODEL_PATH,
    SCALER_PATH
)


def save_artifacts(model, scaler):

    joblib.dump(model, KMEANS_MODEL_PATH)

    joblib.dump(scaler, SCALER_PATH)

    print("Artifacts saved successfully")