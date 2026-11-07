#! /usr/bin/env python3
from collections.abc import Callable
import functools
from time import perf_counter, sleep
from typing import Any
from inspect import signature


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        time_start = perf_counter()
        res = func(*args, **kwargs)
        time_end = perf_counter()
        time_count = time_end - time_start
        print(f"Spell completed in {time_count:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def standalone(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            sig = signature(func)
            parms = list(sig.parameters.keys())
            is_method = len(parms) > 0 and parms[0] in ('self', 'cls')

            if is_method:
                power = args[2] if len(args) >= 3 else kwargs.get('power', 0)
            else:
                power = args[0] if len(args) >= 1 else kwargs.get('power', 0)

            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return standalone


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def verified(func: Callable[..., Any]) -> Any:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts+1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed,\
 retrying... (attempt {attempt}/{max_attempts})")
                    else:
                        return f"Spell casting\
 failed after {max_attempts} attempts"
        return wrapper
    return verified


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power}"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        sleep(0.101)
        return "Result: Fireball Cast!"
    print(fireball())
    print("\nTesting power validator...")

    @power_validator(10)
    def heal(power: int, target: str) -> str:
        return f"Heal restores {target} for {power} HP"
    print(heal(11, "Dragon"))
    print("\nTesting retrying spell...")

    @retry_spell(3)
    def spelled(value: int) -> str:
        if value < 20:
            raise ValueError("It's not enough")
        return "Waaaaaaagh spelled !"

    print(spelled(4))
    print(spelled(21))
    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(mage.validate_mage_name("True"))
    print(mage.validate_mage_name("fl"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 5))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
