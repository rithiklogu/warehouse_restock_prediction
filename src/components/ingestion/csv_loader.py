"""
CSV Loader Component.

Reads a single CSV file using Polars with logging and exception handling.
"""

from pathlib import Path

import polars as pl

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class CSVLoader:
    """
    Load a single CSV file into a Polars DataFrame.
    """

    def __init__(self) -> None:
        logger.info("CSVLoader initialized.")

    def load(self, file_path: Path) -> pl.DataFrame:
        """
        Load a CSV file.

        Args:
            file_path (Path):
                Path to the CSV file.

        Returns:
            pl.DataFrame:
                Loaded dataframe.

        Raises:
            CustomException:
                If loading fails.
        """

        try:

            logger.info(f"Loading file: {file_path}")

            if not file_path.exists():
                raise FileNotFoundError(f"{file_path} does not exist.")

            dataframe = pl.read_csv(file_path)

            logger.success(
                f"Loaded '{file_path.name}' "
                f"Rows={dataframe.height}, "
                f"Columns={dataframe.width}"
            )

            return dataframe

        except Exception as e:
            logger.exception("Failed to load CSV.")
            raise CustomException(e, __import__("sys"))