"""
Rolling Feature Engineering Component.

Creates rolling statistical features used by the forecasting model.
"""

import sys

import polars as pl

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class RollingFeatureEngineer:
    """
    Creates rolling statistical features.

    Current Features
    ----------------
    - avg_sales_3
    """

    def __init__(self) -> None:
        logger.info("RollingFeatureEngineer initialized.")

    def run(
        self,
        dataframe: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        Create rolling features.

        Parameters
        ----------
        dataframe : pl.DataFrame
            DataFrame containing lag features.

        Returns
        -------
        pl.DataFrame
            DataFrame with rolling features added.
        """

        try:
            logger.info("Creating rolling features...")

            dataframe = dataframe.with_columns(
                pl.mean_horizontal(
                    [
                        pl.col("sales_last_1"),
                        pl.col("sales_last_2"),
                        pl.col("sales_last_3"),
                    ]
                ).alias("avg_sales_3")
            )

            logger.success("Rolling features created successfully.")

            return dataframe

        except Exception as e:
            logger.exception("Rolling feature creation failed.")
            raise CustomException(e, sys)