from src.components.ingestion.ingestion import DataIngestion
from src.components.preprocessing.merge_data import MergeData


def main():

    ingestion = DataIngestion()

    datasets = ingestion.run()

    merger = MergeData()

    merged_df = merger.run(datasets)

    print("=" * 80)

    print(merged_df.shape)

    print()

    print(merged_df.head())


if __name__ == "__main__":

    main()