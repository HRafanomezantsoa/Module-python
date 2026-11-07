#! /usr/bin/env python3
from ex0 import FlameFactory, AquaFactory


def test_factory(factory: FlameFactory | AquaFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def battle(
        factory1: FlameFactory | AquaFactory,
        factory2: FlameFactory | AquaFactory) -> None:
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    print("Testing battle")
    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factory(flame)
    test_factory(aqua)
    battle(flame, aqua)
