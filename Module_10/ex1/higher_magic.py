#! /usr/bin/env python3
from collections.abc import Callable
from typing import Any


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(
        spell1: Callable[..., Any],
        spell2: Callable[..., Any]) -> Callable[..., Any]:
    def combined_spell(target: str, power: int) -> tuple[Any, Any]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(
        base_spell: Callable[..., Any], multiplier: int) -> Callable[..., Any]:
    if not isinstance(multiplier, int):
        raise TypeError("The multiplier must be an int")

    def multiplied(target: str, power: int) -> Any:
        return base_spell(target, power * multiplier)
    return multiplied


def condition(target: str, power: int) -> bool:
    return power >= 20


def conditional_caster(
        condition: Callable[..., Any],
        spell: Callable[..., Any]) -> Callable[..., Any]:
    def result_condition(target: str, power: int) -> Any:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzed"
    return result_condition


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} for {power} armor"


def spell_sequence(spells: list[Callable[..., Any]]) -> Callable[..., Any]:
    def all_spell(target: str, power: int) -> list[Any]:
        sequence = []
        for spell in spells:
            result = spell(target, power)
            sequence.append(result)
        return sequence
    return all_spell


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    rs1, res2 = combined("Dragon", 20)
    print(f"Combined spell result: {rs1}, {res2}")
    print("\nTesting power amplifier...")
    try:
        mega_fireball = power_amplifier(fireball, 3)
        print(mega_fireball("Dragon", 10))
    except TypeError as e:
        print(e)
    print("\nTesting conditional caster...")
    cond_caster = conditional_caster(condition, fireball)
    res_caster = cond_caster("Dragon", 20)
    print(res_caster)
    print("\nTesting spell sequence...")
    sequences = spell_sequence([fireball, heal, shield])
    res_sequences = sequences("Dragon", 13)
    for sequence in res_sequences:
        print(sequence)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
