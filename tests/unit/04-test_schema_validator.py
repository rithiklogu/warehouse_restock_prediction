import polars as pl

from src.components.validation.schema_validator import (
    SchemaValidator,
)

validator = SchemaValidator()

df = pl.DataFrame(
    {
        "id": [1, 2],
        "name": ["A", "B"],
    }
)

validator.validate(
    dataframe=df,
    required_columns=[
        "id",
        "name",
    ],
    dataset_name="products",
)

print("Validation Passed")