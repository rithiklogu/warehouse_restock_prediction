from pathlib import Path

from src.components.ingestion.csv_loader import CSVLoader


loader = CSVLoader()

df = loader.load(
    Path("data/raw/Products.csv")
)

print(df.head())

print(df.shape)