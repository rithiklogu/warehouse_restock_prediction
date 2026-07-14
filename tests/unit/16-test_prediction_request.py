from src.schemas.prediction_request import PredictionRequest


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

        opening_stock=200,

        sales_last_1=180,

        sales_last_2=170,

        sales_last_3=160,

        avg_sales_3=170,

        promotion=1,

        discount_percentage=10,

        festival_flag=0,

        returns=4,
    )

    print(request.model_dump())


if __name__ == "__main__":

    main()