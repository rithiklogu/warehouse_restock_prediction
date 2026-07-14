from catboost import CatBoostRegressor

from src.components.ingestion.ingestion import DataIngestion
from src.components.preprocessing.preprocess import Preprocess
from src.components.feature_engineering.feature_builder import (
    FeatureBuilder,
)
from src.components.training.model_trainer import (
    ModelTrainer,
)
from src.components.training.model_evaluator import (
    ModelEvaluator,
)


TARGET = "target_next_month_demand"

FEATURES = ['year',
 'month',
 'product_id',
 'hub_id',
 'category',
 'brand',
 'city',
 'product_name',
 'opening_stock',
 'sales_last_1',
 'sales_last_2',
 'sales_last_3',
 'avg_sales_3',
 'promotion',
 'discount_percentage',
 'festival_flag',
 'returns',
 'target_next_month_demand']

CAT_FEATURES = [
    "product_id",
    "hub_id",
    "category",
    "brand",
    "city",
    "product_name"]




def main():

    datasets = DataIngestion().run()

    dataframe = Preprocess().run(datasets)

    dataframe = FeatureBuilder().run(dataframe)

    X = dataframe.select(FEATURES)

    y = dataframe[TARGET]

    model = CatBoostRegressor(
        iterations=100,
        learning_rate=0.1,
        depth=6,
        loss_function="RMSE",
        random_seed=42,
        verbose=False,
    )

    trainer = ModelTrainer(model)

    trained_model = trainer.run(
        X_train=X,
        y_train=y,
        cat_features=CAT_FEATURES,
    )

    evaluator = ModelEvaluator()

    results = evaluator.run(
        model=trained_model,
        X=X,
        y=y,
    )

    print("=" * 80)

    print("Evaluation Metrics")

    print("=" * 80)

    for metric, value in results["metrics"].items():

        print(f"{metric:<10}: {value:.4f}")

    print()

    print("=" * 80)

    print("Prediction Sample")

    print("=" * 80)

    print(results["predictions"][:10])


if __name__ == "__main__":
    main()