#! /usr/bin/env python3

class Plant:
    class Statistical:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0
            self._shade = 0

        def show_calls(self) -> None:
            self._show += 1

        def grow_calls(self) -> None:
            self._grow += 1

        def age_calls(self) -> None:
            self._age += 1

        def info(self, name: str) -> None:
            print(f"[statistics for {name}]")
            print(f"Stats: {self._grow} grow,\
 {self._age} age, {self._show} show")

    def __init__(self, name: str, height: float | int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self.statistics = self.Statistical()

    @staticmethod
    def Check_year(ages: int) -> bool:
        result = ages > 365
        if result:
            print(f"Is {ages} days more than a year? -> {result}")
            return True
        else:
            print(f"Is {ages} days more than a year? -> {result}")
            return False

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls(name="Unknown plant", height=0, age=0)

    def show(self) -> None:
        print(f"{self._name}: {(self._height):.1f}cm, {self._age} days old")
        self.statistics.show_calls()


class Flower(Plant):
    def __init__(self, name: str,
                 height: float | int,
                 age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def show_color(self) -> None:
        print(f" Color: {self._color}")

    def bloom(self, blom: bool = False) -> None:
        if not blom:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")
            self.statistics.grow_calls()


class Tree(Plant):
    def __init__(self, name: str,
                 height: float | int,
                 age: int,
                 trunk_diameter: float | int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def shade(self, Shade: int = 0) -> None:
        print(f" {Shade} shade")

    def trunk_d(self) -> None:
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of \
{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide.")


class Seed(Flower):
    def __init__(self, name: str,
                 height: float | int,
                 age: int,
                 color: str) -> None:
        super().__init__(name, height, age, color)

    def seed(self, seed: int = 0) -> None:
        self.Seed = seed
        print(f" Seeds: {self.Seed}")

    def infos(self) -> None:
        self.statistics.age_calls()


def display_statistics(plant: Plant) -> None:
    plant.statistics.info(plant._name)


if __name__ == "__main__":
    rose = Flower("Rose", 15, 10, "red")
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.Check_year(30)
    Plant.Check_year(400)
    print()
    print("=== Flower")
    rose.show()
    rose.show_color()
    rose.bloom()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose._height += 8
    rose.show()
    rose.show_color()
    rose.bloom(True)
    display_statistics(rose)
    print()

    print("=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    tree.trunk_d()
    display_statistics(tree)
    tree.shade()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    display_statistics(tree)
    tree.shade(1)

    print()
    see_d = Seed("Sunflower", 80, 45, "yellow")
    print("=== Seed")
    see_d.show()
    see_d.show_color()
    see_d.bloom()
    see_d.seed()
    print("[make sunflower grow, age and bloom]")
    see_d._height += 30
    see_d._age += 20
    see_d.show()
    see_d.show_color()
    see_d.bloom(True)
    see_d.seed(42)
    see_d.infos()
    display_statistics(see_d)
    print()
    Anonymous = Plant.anonymous()
    print("=== Anonymous")
    Anonymous.show()
    display_statistics(Anonymous)
