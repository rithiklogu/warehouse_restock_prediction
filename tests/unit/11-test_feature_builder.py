from src.components.ingestion.ingestion import DataIngestion
from src.components.preprocessing.preprocess import Preprocess

from src.components.feature_engineering.feature_builder import (
    FeatureBuilder,
)


def main():

    datasets = DataIngestion().run()

    dataframe = Preprocess().run(datasets)

    dataframe = FeatureBuilder().run(dataframe)

    print("=" * 100)

    print(dataframe.shape)

    print()

    print(dataframe.head())

    print()

    print(dataframe.columns)


if __name__ == "__main__":
    main()