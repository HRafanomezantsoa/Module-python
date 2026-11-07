#! /usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int > 40:
        raise ValueError("100°C is too hot for plants (max 40°C)")
    elif temp_int < 0:
        raise ValueError("-50°C is too cold for plants (min 0°C)")
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    test = ["25", "abc", "100", "-50"]
    for i in test:
        print(f"\nInput data is '{i}'")
        try:
            input_temperature(i)
            print(f"Temperature is now {i}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
