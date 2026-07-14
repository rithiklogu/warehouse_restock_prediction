"""
Target Builder Component.

Creates the target variable for model training.
"""

import polars as pl

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class TargetBuilder:
    """
    Creates the target column.
    """

    def __init__(self) -> None:

        logger.info("TargetBuilder initialized.")

    def run(
        self,
        dataframe: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        Create the target column.

        Parameters
        ----------
        dataframe : pl.DataFrame

        Returns
        -------
        pl.DataFrame
        """

        try:

            logger.info("Creating target column...")

            dataframe = dataframe.with_columns(

                pl.col("quantity_sold")
                .shift(-1)
                .over(
                    [
                        "product_id",
                        "hub_id",
                    ]
                )
                .alias("target_next_month_demand")

            )

            logger.success(
                "Target column created successfully."
            )

            return dataframe

        except Exception as e:

            logger.exception(
                "Target creation failed."
            )

            raise CustomException(
                e,
                __import__("sys"),
            )