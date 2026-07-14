"""
Application settings.

Loads all YAML configuration files once and exposes them
through a singleton `settings` object.
"""

from pathlib import Path

import yaml
from pydantic import BaseModel

from src.config.paths import CONFIG_DIR


def load_yaml(file_path: Path) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


config = load_yaml(CONFIG_DIR / "config.yaml")
feature_config = load_yaml(CONFIG_DIR / "features.yaml")
model_config = load_yaml(CONFIG_DIR / "model.yaml")
logging_config = load_yaml(CONFIG_DIR / "logging.yaml")


class settings(BaseModel):

    random_state: int
    target_column: str
    log_level: str

    datasets: dict[str, str]

    config: dict
    features: dict
    model: dict
    logging: dict

    @property
    def feature_columns(self) -> list[str]:
        return self.features["feature_columns"]

    @property
    def categorical_features(self) -> list[str]:
        return self.features["categorical_features"]

    @property
    def numerical_features(self) -> list[str]:
        return self.features["numerical_features"]

    @property
    def model_params(self) -> dict:
        return self.model["parameters"]


settings = settings(
    random_state=config["random_state"],
    target_column=config["target_column"],
    log_level=config["log_level"],
    datasets=config["datasets"],
    config=config,
    features=feature_config,
    model=model_config,
    logging=logging_config,
)