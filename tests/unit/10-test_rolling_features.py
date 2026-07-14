from src.components.ingestion.ingestion import DataIngestion
from src.components.preprocessing.preprocess import Preprocess

from src.components.feature_engineering.lag_features import (
    LagFeatureEngineer,
)
from src.components.feature_engineering.target_builder import (
    TargetBuilder,
)
from src.components.feature_engineering.rolling_features import (
    RollingFeatureEngineer,
)


def main():

    datasets = DataIngestion().run()

    dataframe = Preprocess().run(datasets)

    dataframe = LagFeatureEngineer().run(dataframe)

    dataframe = TargetBuilder().run(dataframe)

    dataframe = RollingFeatureEngineer().run(dataframe)

    print(
        dataframe.select(
            [
                "sales_last_1",
                "sales_last_2",
                "sales_last_3",
                "avg_sales_3",
            ]
        ).head(10)
    )


if __name__ == "__main__":
    main()