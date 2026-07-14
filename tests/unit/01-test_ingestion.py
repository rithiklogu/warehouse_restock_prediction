from src.components.ingestion.ingestion import DataIngestion


def main():

    ingestion = DataIngestion()

    datasets = ingestion.run()

    print("=" * 80)

    print("Loaded Datasets")

    print("=" * 80)

    for name, dataframe in datasets.items():

        print(f"{name}")

        print(f"Rows    : {dataframe.height}")

        print(f"Columns : {dataframe.width}")

        print("-" * 40)


if __name__ == "__main__":

    main()