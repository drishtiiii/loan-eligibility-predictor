from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ARTIFACT_DIR = BASE_DIR / "artifacts"

MODEL_PATH = ARTIFACT_DIR / "model.pkl"

SCALER_PATH = ARTIFACT_DIR / "scaler.pkl"

FEATURE_COLUMNS_PATH = ARTIFACT_DIR / "feature_columns.pkl"