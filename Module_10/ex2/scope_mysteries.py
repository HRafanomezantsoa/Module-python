#! /usr/bin/env python3
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[..., Any]:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter
    return count


def spell_accumulator(initial_power: int) -> Callable[..., Any]:
    base: int = initial_power

    def accumulator(add: int) -> int:
        nonlocal base
        base += add
        return base
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[..., Any]:
    def enchantment(value: str) -> str:
        return f"{enchantment_type} {value}"
    return enchantment


def memory_vault() -> dict[str, Callable[..., Any]]:
    memories = {}

    def store(key: str, value: Any) -> str:
        memories[key] = value
        return f"Store '{key}' = {memories[key]}"

    def recall(key: str) -> str:
        if key in memories:
            return f"Recall '{key}': {memories[key]}"
        else:
            return f"Recall '{key}': Memory not found"
    return {'store': store, 'recall': recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    for i in range(1, 3):
        print(f"counter_a call {i}: {counter_a()}")
    counter_b = mage_counter()
    for i in range(1, 2):
        print(f"counter_b call {i}: {counter_b()}")
    print("\nTesting spell accumulator...")
    initial: int = 100
    accumul = spell_accumulator(initial)
    print(f"Base {initial}, add {20}: {accumul(20)}")
    print(f"Base {initial}, add {30}: {accumul(30)}")
    print("\nTesting enchantment factory...")
    dict_enchantment: dict[str, str] = {
        "Earthen": "Sword",
        "Windy": "Ring",
        "Shocking": "Wand"
    }
    for key, value in dict_enchantment.items():
        the_enchantment = enchantment_factory(key)
        print(the_enchantment(value))
    print("\nTesting memory vault...")
    vault = memory_vault()
    print(vault['store']("secret", 42))
    print(vault['recall']("secret"))
    print(vault['recall']('unknown'))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
