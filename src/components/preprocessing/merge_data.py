"""
Merge Data Component.

This component is responsible for merging all raw datasets into a
single dataframe for downstream preprocessing.

Flow:
    Sales
        ↓
    Join Products
        ↓
    Join Warehouses
        ↓
    Join Inventory
"""

from typing import Dict

import polars as pl

from src.exception.custom_exception import CustomException
from src.logger.logger import logger


class MergeData:
    """
    Merge all raw datasets into a single dataframe.

    Expected datasets
    -----------------
    products
    warehouses
    sales
    inventory
    """

    def __init__(self) -> None:
        logger.info("MergeData initialized.")

    def run(
        self,
        datasets: Dict[str, pl.DataFrame],
    ) -> pl.DataFrame:
        """
        Merge datasets.

        Parameters
        ----------
        datasets : dict[str, pl.DataFrame]

        Returns
        -------
        pl.DataFrame
            Merged dataframe.
        """

        try:

            logger.info("Starting dataset merge...")

            sales_df = datasets["sales"]
            products_df = datasets["products"]
            warehouses_df = datasets["warehouses"]
            inventory_df = datasets["inventory"]

            merged_df = (
                sales_df
                .join(
                    products_df,
                    on="product_id",
                    how="left",
                )
                .join(
                    warehouses_df,
                    on="hub_id",
                    how="left",
                )
                .join(
                    inventory_df,
                    on=["hub_id", "product_id"],
                    how="left",
                )
            )

            logger.success(
                f"Merged dataframe created successfully "
                f"(Rows={merged_df.height}, "
                f"Columns={merged_df.width})"
            )

            return merged_df

        except Exception as e:

            logger.exception("Dataset merge failed.")

            raise CustomException(e, __import__("sys"))