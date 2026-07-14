from src.schemas.prediction_response import PredictionResponse


def main():

    response = PredictionResponse(

        predicted_demand=185,

        current_stock=120,

        remaining_stock=-65,

        safety_stock=50,

        restock_required=True,

        recommended_order_quantity=115,

        recommendation="Restock immediately",

        confidence=96.84,
    )

    print(response.model_dump())


if __name__ == "__main__":

    main()