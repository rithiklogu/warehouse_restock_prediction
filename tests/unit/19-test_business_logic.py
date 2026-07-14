from src.components.prediction.business_logic import BusinessLogic


def main():

    result = BusinessLogic().run(
        predicted_demand=185.4,
        current_stock=120,
    )

    print()

    for key, value in result.model_dump().items():
        print(f"{key:<30}: {value}")


if __name__ == "__main__":
    main()