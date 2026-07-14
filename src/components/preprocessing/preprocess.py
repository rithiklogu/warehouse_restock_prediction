"""
Preprocessing Pipeline Component.

Coordinates all preprocessing steps.
"""

import polars as pl

from src.components.preprocessing.clean_data import CleanData
from src.components.preprocessing.merge_data import MergeData
from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class Preprocess:
    """
    Execute the preprocessing workflow.
    """

    def __init__(self) -> None:

        self.cleaner = CleanData()

        self.merger = MergeData()

        logger.info("Preprocess initialized.")

    def run(
        self,
        datasets: dict[str, pl.DataFrame],
    ) -> pl.DataFrame:
        """
        Execute preprocessing.

        Parameters
        ----------
        datasets
            Dictionary containing raw datasets.

        Returns
        -------
        pl.DataFrame
            Merged dataframe ready for feature engineering.
        """

        try:

            logger.info("Starting preprocessing...")

            datasets = self.cleaner.run(datasets)

            merged_df = self.merger.run(datasets)

            logger.success("Preprocessing completed successfully.")

            return merged_df

        except Exception as e:

            logger.exception("Preprocessing failed.")

            raise CustomException(e, __import__("sys"))