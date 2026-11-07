#! /usr/bin/env python3

class Plant:
    def __init__(self,
                 name: str,
                 height: float,
                 ages: int,
                 growth: float) -> None:
        self.name = name
        self.height = height
        self.ages = ages
        self.growth = growth

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.ages += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1):.1f}cm, \
{self.ages} days old")

    def s_growth(self) -> None:
        i_height = self.height
        print("=== Garden Plant Growth ===")
        self.show()
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            self.grow()
            self.age()
            self.show()
        print(f"Gwoth this week: {round(self.height - i_height, 1)}cm")


if __name__ == "__main__":
    Rose = Plant("Rose", 25.0, 30, 0.8)
    Rose.s_growth()
