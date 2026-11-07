#! /usr/bin/env python3
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda artifact: artifact['power'],
                  reverse=True)


def power_filter(
        mages: list[dict[str, Any]], min_power: int) -> list[dict[str, Any]]:
    the_filter = filter(lambda mage: mage['power'] >= min_power, mages)
    return list(the_filter)


def spell_transformer(spells: list[str]) -> list[str]:
    if not spells:
        print("Empty spell")
    the_spells = map(lambda spell: "* " + spell + " *", spells)
    return list(the_spells)


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    the_max = max(mages, key=lambda x: x['power'])['power']
    the_min = min(mages, key=lambda x: x['power'])['power']
    the_sum = sum(x['power'] for x in mages)
    the_average = round(the_sum / len(mages), 2)
    return {
        "max_power": the_max,
        "min_power": the_min,
        "avg_power": the_average
    }


def main() -> None:
    artifacts = [
        {'name': 'Light Prism', 'power': 63, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 111, 'type': 'weapon'},
        {'name': 'Ice Wand', 'power': 69, 'type': 'relic'}
    ]
    print("\nTesting artifact sorter...")
    sorters = artifact_sorter(artifacts)
    for sorter in sorters:
        print(sorter)

    print("\nTesting power filter...")
    print(power_filter(artifacts, 70))

    spells: list[str] = ["fireball", "heal", "shield"]
    print("\nTesting spell transformer...")
    result = spell_transformer(spells)
    print(*result)

    stats = mage_stats(artifacts)
    print("\nStatistics...")
    print(f"Most powerful mage's power level: {stats['max_power']}")
    print(f"Least powerful mage's power level: {stats['min_power']}")
    print(f"Average power level: {stats['avg_power']}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
