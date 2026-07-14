"""
Model Saver.
"""

import json
import sys
from datetime import datetime

from src.components.persistence.artifact_manager import ArtifactManager
from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class ModelSaver:

    def __init__(self):

        self.artifacts = ArtifactManager()

        logger.info("ModelSaver initialized.")

    def run(
        self,
        model,
        metrics: dict,
        feature_columns: list[str],
    ) -> None:

        try:

            logger.info("Saving trained model...")

            model.save_model(
                str(self.artifacts.model_path)
            )

            logger.success(
                f"Model saved -> {self.artifacts.model_path}"
            )

            with open(
                self.artifacts.metrics_path,
                "w",
            ) as f:

                json.dump(
                    metrics,
                    f,
                    indent=4,
                )

            logger.success(
                "Metrics saved."
            )

            with open(
                self.artifacts.feature_path,
                "w",
            ) as f:

                json.dump(
                    feature_columns,
                    f,
                    indent=4,
                )

            metadata = {

                "model": "CatBoostRegressor",

                "created_at": datetime.now().isoformat(),

                "version": "1.0.0",

            }

            with open(
                self.artifacts.metadata_path,
                "w",
            ) as f:

                json.dump(
                    metadata,
                    f,
                    indent=4,
                )

            logger.success(
                "Artifacts saved successfully."
            )

        except Exception as e:

            logger.exception(
                "Saving model failed."
            )

            raise CustomException(
                e,
                sys,
            )