from src.components.ingestion.ingestion import DataIngestion
from src.components.preprocessing.preprocess import Preprocess

from src.components.feature_engineering.lag_features import (
    LagFeatureEngineer,
)

from src.components.feature_engineering.target_builder import (
    TargetBuilder,
)


def main():

    datasets = DataIngestion().run()

    dataframe = Preprocess().run(datasets)

    dataframe = LagFeatureEngineer().run(dataframe)

    dataframe = TargetBuilder().run(dataframe)

    print(
        dataframe.select(
            [
                "quantity_sold",
                "target_next_month_demand",
            ]
        ).head(15)
    )


if __name__ == "__main__":

    main()