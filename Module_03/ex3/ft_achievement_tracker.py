#! /usr/bin/env python3
import random


def get_player_achievements() -> set:
    all_achievement = ['Crafting Genius', 'World Savior', 'Master Explorer',
                       'Collector Supreme', 'Untouchable', 'Boss Slayer',
                       'Strategist', 'Speed Runner', 'Survivor',
                       'Treasure Hunter', 'Unstoppable', 'Hidden Path Finder',
                       'First Steps', 'Sharp Mind']
    set_achievement = set()
    size = random.randint(0, len(all_achievement))
    for n in range(size):
        set_achievement.add(random.choice(all_achievement))
    return set_achievement


def main() -> None:
    player_alice: dict = {
        "name": "Alice",
        "achivements": get_player_achievements()
    }

    player_bob: dict = {
        "name": "Bob",
        "achivements": get_player_achievements()
    }
    player_charlie: dict = {
        "name": "Charlie",
        "achivements": get_player_achievements()
    }
    player_dylan: dict = {
        "name": "Dylan",
        "achivements": get_player_achievements()
    }
    all_name = [player_alice, player_bob, player_charlie, player_dylan]
    for name in all_name:
        print(f"Player {name["name"]}: {name["achivements"]}")
    all_distinct = player_alice["achivements"].union(
        player_bob["achivements"], player_charlie["achivements"],
        player_dylan["achivements"])
    print()
    print(f"All distinct achievements: {all_distinct}")
    common = player_alice["achivements"].intersection(
        player_bob["achivements"],
        player_charlie["achivements"],
        player_dylan["achivements"])
    print()
    print(f"Common achievements: {common}")
    print()
    only_alice = player_alice["achivements"].difference(
        player_bob["achivements"],
        player_charlie["achivements"],
        player_dylan["achivements"])
    only_bob = player_bob["achivements"].difference(
        player_alice["achivements"],
        player_charlie["achivements"],
        player_dylan["achivements"])
    only_charlie = player_charlie["achivements"].difference(
        player_bob["achivements"],
        player_alice["achivements"],
        player_dylan["achivements"])
    only_dylan = player_dylan["achivements"].difference(
        player_bob["achivements"],
        player_charlie["achivements"],
        player_alice["achivements"])
    diff = [only_alice, only_bob, only_charlie, only_dylan]
    i = 0
    for name in all_name:
        print(f"Only {name["name"]} has: {diff[i]}")
        i += 1
    print()
    all_achievement = ['Crafting Genius', 'World Savior', 'Master Explorer',
                       'Collector Supreme', 'Untouchable', 'Boss Slayer',
                       'Strategist', 'Speed Runner', 'Survivor',
                       'Treasure Hunter', 'Unstoppable', 'Hidden Path Finder',
                       'First Steps', 'Sharp Mind']
    miss_alice = set(all_achievement) - player_alice["achivements"]
    miss_bob = set(all_achievement) - player_bob["achivements"]
    miss_charlie = set(all_achievement) - player_charlie["achivements"]
    miss_dylan = set(all_achievement) - player_dylan["achivements"]
    miss = [miss_alice, miss_bob, miss_charlie, miss_dylan]
    i = 0
    for name in all_name:
        print(f"{name["name"]} is missing: {miss[i]}")
        i += 1


if __name__ == "__main__":
    print("=== Achievement Tracker System ====\n")
    main()
