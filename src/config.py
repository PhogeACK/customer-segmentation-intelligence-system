from pathlib import Path

# Root project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Data paths
DATA_PATH = BASE_DIR / "data" / "marketing_campaign.csv"

# Model paths
MODEL_DIR = BASE_DIR / "models"

KMEANS_MODEL_PATH = MODEL_DIR / "kmeans_model.pkl"
SCALER_PATH = MODEL_DIR / "scaler.pkl"
CLUSTER_PROFILE_PATH = MODEL_DIR / "cluster_profiles.pkl"

# Output paths
OUTPUT_DIR = BASE_DIR / "outputs"

PREDICTION_OUTPUT_PATH = OUTPUT_DIR / "segmentation_results.csv"