"""
Lag Feature Engineering Component.

Creates lag-based demand features.
"""

import polars as pl

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class LagFeatureEngineer:

    def __init__(self):

        logger.info(
            "LagFeatureEngineer initialized."
        )

    def run(
        self,
        dataframe: pl.DataFrame,
    ) -> pl.DataFrame:

        try:

            logger.info(
                "Creating lag features..."
            )

            dataframe = dataframe.sort(
                [
                    "product_id",
                    "hub_id",
                    "year",
                    "month",
                ]
            )

            dataframe = dataframe.with_columns(

                pl.col("quantity_sold")
                .shift(1)
                .over(
                    [
                        "product_id",
                        "hub_id",
                    ]
                )
                .alias("sales_last_1"),

                pl.col("quantity_sold")
                .shift(2)
                .over(
                    [
                        "product_id",
                        "hub_id",
                    ]
                )
                .alias("sales_last_2"),

                pl.col("quantity_sold")
                .shift(3)
                .over(
                    [
                        "product_id",
                        "hub_id",
                    ]
                )
                .alias("sales_last_3"),

            )

            logger.success(
                "Lag features created."
            )

            return dataframe

        except Exception as e:

            logger.exception(
                "Lag feature engineering failed."
            )

            raise CustomException(
                e,
                __import__("sys"),
            )