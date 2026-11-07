#! /usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        rounde = round(self.height, 1)
        print(f"Created: {self.name}: {rounde:.1f}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    Rose = Plant("Rose", 25.12, 30)
    Rose.show()
    Oak = Plant("Oak", 200.0000, 365)
    Oak.show()
    Cactus = Plant("Cactus", 5, 90)
    Cactus.show()
    Sunflower = Plant("Sunflower", 80, 45)
    Sunflower.show()
    Fern = Plant("Fern", 15, 120)
    Fern.show()
