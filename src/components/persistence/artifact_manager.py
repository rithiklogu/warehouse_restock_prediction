"""
Artifact Manager.

Centralized artifact path management.
"""

from pathlib import Path

from src.config.paths import ARTIFACTS_DIR
from src.logger.logger import logger


class ArtifactManager:
    """
    Handles artifact paths.
    """

    def __init__(self) -> None:

        self.artifacts_dir = Path(ARTIFACTS_DIR)

        self.artifacts_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        logger.info("ArtifactManager initialized.")

    @property
    def model_path(self) -> Path:
        return self.artifacts_dir / "catboost_model.cbm"

    @property
    def metrics_path(self) -> Path:
        return self.artifacts_dir / "metrics.json"

    @property
    def feature_path(self) -> Path:
        return self.artifacts_dir / "feature_columns.json"

    @property
    def metadata_path(self) -> Path:
        return self.artifacts_dir / "metadata.json"