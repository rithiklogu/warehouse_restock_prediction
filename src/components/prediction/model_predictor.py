"""
Prediction component.

Responsible for generating demand predictions using
the trained CatBoost model.
"""

import sys

import polars as pl

from src.config.settings import settings

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class Predictor:
    """
    Predictor component.
    """

    def __init__(self):

        logger.info("Predictor initialized.")

    def run(
        self,
        model,
        request,
    ) -> float:

        try:

            logger.info(
                "Preparing prediction dataframe..."
            )

            dataframe = pl.DataFrame(
                [request.model_dump()]
            )

            dataframe = dataframe.select(
                settings.feature_columns
            )

            logger.info(
                "Generating prediction..."
            )

            prediction = model.predict(
                dataframe.to_pandas()
            )[0]

            logger.success(
                f"Prediction completed: {prediction:.2f}"
            )

            return float(prediction)

        except Exception as e:

            logger.exception(
                "Prediction failed."
            )

            raise CustomException(
                e,
                sys,
            )