from src.components.ingestion.ingestion import DataIngestion
from src.components.preprocessing.preprocess import Preprocess


def main():

    ingestion = DataIngestion()

    datasets = ingestion.run()

    preprocess = Preprocess()

    merged_df = preprocess.run(datasets)

    print("=" * 80)

    print(merged_df.shape)

    print()

    print(merged_df.head())


if __name__ == "__main__":

    main()