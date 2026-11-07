#! /usr/bin/env python3
import random


def ft_data_alchemist() -> None:
    initial_players = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {initial_players}")
    all_cap = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {all_cap}")
    cap_only = [name for name in initial_players if name[0].isupper()]
    print(f"New list of capitalized names only: {cap_only}")
    scores = {name: random.randint(1, 1000) for name in all_cap}
    print(f"Score dict: {scores}")
    average = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")
    high_scores = {
        name: score for name, score in scores.items() if score > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    ft_data_alchemist()
