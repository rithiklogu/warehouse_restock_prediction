from src.schemas.prediction_request import PredictionRequest

from src.components.persistence.model_loader import (
    ModelLoader,
)

from src.components.prediction.model_predictor import (
    Predictor,
)


def main():

    request = PredictionRequest(

        year=2026,

        month=7,

        product_id=101,

        hub_id=1,

        category="Electronics",

        brand="Samsung",

        city="Chennai",

        product_name="Samsung Galaxy",

        opening_stock=250,

        sales_last_1=180,

        sales_last_2=170,

        sales_last_3=160,

        avg_sales_3=170,

        promotion=1,

        discount_percentage=10,

        festival_flag=0,

        returns=5,
    )

    model = ModelLoader().run()

    prediction = Predictor().run(

        model=model,

        request=request,
    )

    print(f"\nPrediction : {prediction:.2f}")


if __name__ == "__main__":

    main()