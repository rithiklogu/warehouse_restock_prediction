from src.components.ingestion.ingestion import DataIngestion
from src.components.preprocessing.clean_data import CleanData


def main():

    ingestion = DataIngestion()

    datasets = ingestion.run()

    cleaner = CleanData()

    datasets = cleaner.run(datasets)

    print(datasets["sales"].dtypes)

    print(datasets["inventory"].dtypes)


if __name__ == "__main__":

    main()