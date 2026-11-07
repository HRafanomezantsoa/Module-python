#! /usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float | int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        if self._age < 0:
            self._age = 0
        print(f"{self._name}: {(self._height):.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str,
                 height: float | int,
                 age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def show_color(self) -> None:
        print(f" Color: {self._color}")

    def bloom(self, blom: bool = False) -> None:
        if not blom:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str,
                 height: float | int,
                 age: int,
                 trunk_d: float | int) -> None:
        super().__init__(name, height, age)
        self._trunk_d = trunk_d

    def trunk_diameter(self) -> None:
        print(f" Trunk diameter: {self._trunk_d:.1f}cm")

    def produce_shabe(self) -> None:
        print(f"Tree {self._name} now produces a shade of \
{self._height:.1f}cm long and {self._trunk_d:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str,
                 height: float | int,
                 age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season

    def nutritional_v(self, nutritional_value: int = 0) -> None:
        if nutritional_value == 0:
            print(f" Nutritional value: {nutritional_value}")
        else:
            for day in range(1, 10, 10):
                nutritional_value += 10
            print(f" Nutritional value: {nutritional_value}")

    def grow(self) -> None:
        for i in range(1, 20, 10):
            self._height += 21

    def v_age(self) -> None:
        self._age += 20

    def harvest_s(self) -> None:
        print(f" Harvest season: {self._harvest_season}")


if __name__ == "__main__":
    rose = Flower("Rose", 15, -10, "red")
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    rose.show_color()
    rose.bloom()
    print("[asking the rose to bloom]")
    rose.show()
    rose.show_color()
    rose.bloom(True)
    print()
    print("=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    tree.trunk_diameter()
    print("[asking the oak to produce shade]")
    tree.produce_shabe()
    print()
    vegetable = Vegetable("Tomato", 5, 10, "April")
    print("=== Vegetable")
    vegetable.show()
    vegetable.harvest_s()
    vegetable.nutritional_v()
    print("[make tomato grow and age for 20 days]")
    vegetable.grow()
    vegetable.v_age()
    vegetable.show()
    vegetable.harvest_s()
    vegetable.nutritional_v(10)
