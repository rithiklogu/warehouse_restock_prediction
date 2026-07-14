"""
Time Series Split Component.

Splits the feature engineered dataset into
training, validation and testing datasets.
"""

import sys

import polars as pl

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class TimeSeriesSplitter:
    """
    Split feature engineered dataset into
    train, validation and test datasets.
    """

    def __init__(self) -> None:

        logger.info("TimeSeriesSplitter initialized.")

    def run(
        self,
        dataframe: pl.DataFrame,
        train_ratio: float = 0.70,
        validation_ratio: float = 0.15,
    ) -> tuple[
        pl.DataFrame,
        pl.DataFrame,
        pl.DataFrame,
    ]:

        try:

            logger.info(
                "Performing time series split..."
            )

            total_rows = dataframe.height

            train_end = int(total_rows * train_ratio)

            validation_end = train_end + int(
                total_rows * validation_ratio
            )

            train_df = dataframe.slice(
                0,
                train_end,
            )

            validation_df = dataframe.slice(
                train_end,
                validation_end - train_end,
            )

            test_df = dataframe.slice(
                validation_end,
            )

            logger.success(
                f"Train={train_df.height}, "
                f"Validation={validation_df.height}, "
                f"Test={test_df.height}"
            )

            return (
                train_df,
                validation_df,
                test_df,
            )

        except Exception as e:

            logger.exception(
                "Dataset splitting failed."
            )

            raise CustomException(
                e,
                sys,
            )