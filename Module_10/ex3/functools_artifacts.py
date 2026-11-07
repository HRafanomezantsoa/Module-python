#! /usr/bin/env python3
import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return functools.reduce(operator.add, spells)
    elif operation == "multiply":
        return functools.reduce(operator.mul, spells)
    elif operation == "max":
        return max(spells)
    elif operation == "min":
        return min(spells)
    else:
        raise ValueError(f"Operation unknown : {operation}")


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Enchantment {element} of power {power} on {target}"


def partial_enchanter(
        base_enchantment: Callable[..., Any]) -> dict[str, Callable[..., Any]]:
    enchant_fire = functools.partial(base_enchantment, 50, "fire")
    enchant_ice = functools.partial(base_enchantment, 50, "ice")
    enchant_lightning = functools.partial(base_enchantment, 50, "ligthning")

    return {
        "fire": enchant_fire,
        "ice": enchant_ice,
        "lightning": enchant_lightning
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast_spell(value: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @cast_spell.register(str)
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @cast_spell.register(list)
    def _(value: list[Any]) -> str:
        return f"Multi-cast: {len(value)} spells"

    @cast_spell.register(bool)
    def _(value: bool) -> str:
        return "Unknown spell type"
    return cast_spell


def main() -> None:
    print("\nTesting spell reducer...")
    spell_power = [40, 27, 20, 27, 41, 28]
    try:
        print("Sum:", spell_reducer(spell_power, "add"))
        print("Product:", spell_reducer(spell_power, "multiply"))
        print("Max:", spell_reducer(spell_power, "max"))
        print("Min:", spell_reducer(spell_power, "min"))
    except ValueError as e:
        print(e)
    print("\nTesting partial enchanter...")
    enchantment = partial_enchanter(base_enchantment)
    print(enchantment['fire']("Dragon"))
    print(enchantment['ice']("Golem"))
    print(enchantment['lightning']("Ship"))
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fire", "heal", "lightning"]))
    print(dispatcher(10.3))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
