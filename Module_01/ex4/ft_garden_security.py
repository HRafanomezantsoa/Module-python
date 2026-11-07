#! /usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_height(self, height_u: float) -> None:
        self._height = height_u

    def get_age(self, age_u: int) -> None:
        self._age = age_u

    def set_age(self, age_u: int) -> None:
        if age_u < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            print(f"Age updated: {round(age_u, 1)} days")
            self.get_age(age_u)

    def set_height(self, height_u: float) -> None:
        if height_u < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            print(f"Height updated: {round(height_u, 1)}cm")
            self.get_height(height_u)

    def show(self) -> None:
        rounde = round(self._height, 1)
        print("=== Garden Security System ===")
        print(f"Created: {self._name}: {rounde:.1f}cm, {self._age} days old")


if __name__ == "__main__":
    Rose = Plant("Rose", 15, 10)
    Rose.show()
    print()
    Rose.set_height(25)
    Rose.set_age(30)
    print()
    Rose.set_height(-25)
    Rose.set_age(-30)
    print()
    print(f"Current state: {Rose._name}:\
 {Rose._height:.1f}cm, {Rose._age} days old")
