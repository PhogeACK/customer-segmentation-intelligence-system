from src.load_data import load_data
from src.preprocess import preprocess_data
from src.feature_engineering import engineer_features
from src.encoding import encode_features
from src.transform import transform_data
from src.clustering import train_kmeans
from src.save_artifacts import save_artifacts

from src.config import (
    DATA_PATH,
    KMEANS_MODEL_PATH,
    SCALER_PATH
)


def train_pipeline():

    # ---------------------------------
    # Load raw data
    # ---------------------------------
    df = load_data()

    print("Raw data loaded")

    # ---------------------------------
    # Preprocessing
    # ---------------------------------
    df = preprocess_data(df)

    print("Preprocessing completed")

    # ---------------------------------
    # Feature engineering
    # ---------------------------------
    df = engineer_features(df)

    print("Feature engineering completed")

    # ---------------------------------
    # Feature encoding
    # ---------------------------------
    df = encode_features(df)

    print("Feature encoding completed")

    # ---------------------------------
    # Transform + scale
    # ---------------------------------
    df_scaled, scaler = transform_data(df)

    print("Transformations completed")

    # ---------------------------------
    # Train clustering model
    # ---------------------------------
    kmeans_model = train_kmeans(df_scaled)

    print(type(kmeans_model))

    print("KMeans training completed")

    # ---------------------------------
    # Save artifacts
    # ---------------------------------
    save_artifacts(
    model=kmeans_model,
    scaler=scaler
    )

    print("Artifacts saved successfully")


if __name__ == "__main__":

    train_pipeline()