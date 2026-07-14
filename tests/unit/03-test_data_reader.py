from src.components.ingestion.data_reader import DataReader

reader = DataReader()

datasets = reader.read_all()

print(datasets.keys())

for name, df in datasets.items():
    print(f"{name}: {df.shape}")