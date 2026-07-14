from src.components.ingestion.ingestion import DataIngestion
from src.components.preprocessing.preprocess import Preprocess

from src.components.feature_engineering.lag_features import (
    LagFeatureEngineer,
)


def main():

    datasets = DataIngestion().run()

    merged_df = Preprocess().run(datasets)

    lag = LagFeatureEngineer()

    dataframe = lag.run(merged_df)

    print(
        dataframe.select(
            [
                "quantity_sold",
                "sales_last_1",
                "sales_last_2",
                "sales_last_3",
            ]
        ).head(15)
    )


if __name__ == "__main__":

    main()