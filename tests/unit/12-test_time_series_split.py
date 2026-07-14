from src.components.ingestion.ingestion import DataIngestion
from src.components.preprocessing.preprocess import Preprocess
from src.components.feature_engineering.feature_builder import (
    FeatureBuilder,
)
from src.components.splitting.time_series_split import (
    TimeSeriesSplitter,
)


def main():

    datasets = DataIngestion().run()

    dataframe = Preprocess().run(datasets)

    dataframe = FeatureBuilder().run(dataframe)

    splitter = TimeSeriesSplitter()

    train_df, validation_df, test_df = splitter.run(
        dataframe
    )

    print("=" * 80)

    print(f"Train      : {train_df.shape}")

    print(f"Validation : {validation_df.shape}")

    print(f"Test       : {test_df.shape}")


if __name__ == "__main__":

    main()