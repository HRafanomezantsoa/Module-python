#! /usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def custom_errors(wilting: bool, water: int) -> None:
    if wilting:
        raise PlantError("The tomato plant is wilting!")
    if water < 2:
        raise WaterError("Not enough water in the tank!")


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        custom_errors(True, 1)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    try:
        print("\nTesting WaterError...")
        custom_errors(False, 1)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        custom_errors(True, 4)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        custom_errors(False, 1)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
