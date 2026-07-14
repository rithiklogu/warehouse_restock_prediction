"""
Model Loader.
"""

import sys

from catboost import CatBoostRegressor

from src.components.persistence.artifact_manager import ArtifactManager
from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class ModelLoader:

    def __init__(self):

        self.artifacts = ArtifactManager()

        logger.info("ModelLoader initialized.")

    def run(self):

        try:

            logger.info("Loading trained model...")

            model = CatBoostRegressor()

            model.load_model(
                str(
                    self.artifacts.model_path
                )
            )

            logger.success(
                "Model loaded successfully."
            )

            return model

        except Exception as e:

            logger.exception(
                "Model loading failed."
            )

            raise CustomException(
                e,
                sys,
            )