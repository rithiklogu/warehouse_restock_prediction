"""
Feature Engineering Pipeline.

Orchestrates all feature engineering components.
"""

import sys

import polars as pl

from src.components.feature_engineering.lag_features import (
    LagFeatureEngineer,
)
from src.components.feature_engineering.target_builder import (
    TargetBuilder,
)
from src.components.feature_engineering.rolling_features import (
    RollingFeatureEngineer,
)
from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class FeatureBuilder:
    """
    Executes the complete feature engineering pipeline.
    """

    def __init__(self) -> None:

        self.lag_engineer = LagFeatureEngineer()

        self.target_builder = TargetBuilder()

        self.rolling_engineer = RollingFeatureEngineer()

        logger.info("FeatureBuilder initialized.")

    def run(
        self,
        dataframe: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        Build all training features.

        Parameters
        ----------
        dataframe : pl.DataFrame

        Returns
        -------
        pl.DataFrame
        """

        try:

            logger.info("Starting feature engineering...")

            dataframe = self.lag_engineer.run(dataframe)

            dataframe = self.target_builder.run(dataframe)

            dataframe = self.rolling_engineer.run(dataframe)

            logger.info("Removing null values...")

            dataframe = dataframe.drop_nulls()

            logger.success(
                f"Feature engineering completed. "
                f"Rows={dataframe.height}, "
                f"Columns={dataframe.width}"
            )

            return dataframe

        except Exception as e:

            logger.exception(
                "Feature engineering failed."
            )

            raise CustomException(e, sys)