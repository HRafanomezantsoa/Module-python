#! /usr/bin/env python3

def ft_garden_intro(name: str, height: float, age: int) -> None:
    print("=== welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro("Rose", 25, 30)
