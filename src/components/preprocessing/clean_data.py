"""
Data Cleaning Component.

Responsible for datatype conversion.

This component does NOT:
    - remove duplicates
    - fill null values
    - engineer features

Those responsibilities belong to other components.
"""

from typing import Dict

import polars as pl

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class CleanData:
    """
    Perform basic datatype conversion.
    """

    def __init__(self) -> None:

        logger.info("CleanData initialized.")

    def run(
        self,
        datasets: Dict[str, pl.DataFrame],
    ) -> Dict[str, pl.DataFrame]:

        try:

            logger.info("Starting datatype conversion...")

            sales = datasets["sales"]

            inventory = datasets["inventory"]

            sales = sales.with_columns(
                [
                    pl.col("year").cast(pl.Int16),

                    pl.col("month").cast(pl.Int8),

                    pl.col("opening_stock").cast(pl.Int32),

                    pl.col("closing_stock").cast(pl.Int32),

                    pl.col("quantity_sold").cast(pl.Int32),

                    pl.col("promotion").cast(pl.Int8),

                    pl.col("festival_flag").cast(pl.Int8),

                    pl.col("returns").cast(pl.Int32),

                    pl.col("discount_percentage").cast(pl.Float32),
                ]
            )

            inventory = inventory.with_columns(
                pl.col("current_stock").cast(pl.Int32)
            )

            datasets["sales"] = sales

            datasets["inventory"] = inventory

            logger.success(
                "Datatype conversion completed."
            )

            return datasets

        except Exception as e:

            logger.exception(
                "Datatype conversion failed."
            )

            raise CustomException(
                e,
                __import__("sys"),
            )