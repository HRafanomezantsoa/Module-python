#! /usr/bin/env python3

class PlantError(Exception):
    def __init__(self, message: str = "Unknown plant Error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    valid = ["Tomato", "Lettuce", "Carrots"]
    invalid = ["Tomato", "lettuce", "Carrots"]
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for test in valid:
            water_plant(test)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for test in invalid:
            water_plant(test)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
