from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

CONFIG_DIR = PROJECT_ROOT / "config"

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

INTERIM_DATA_DIR = DATA_DIR / "interim"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

PREDICTIONS_DIR = DATA_DIR / "predictions"

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

LOG_DIR = PROJECT_ROOT / "logs"