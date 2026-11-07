#! /usr/bin/env python3
import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run", "eat", "sleep", "grab",
        "move", "climb", "swim", "release"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    event_list: typing.List[tuple[str, str]]) -> typing.Generator[
        tuple[str, str], None, None]:
    while len(event_list) > 0:
        index = random.randrange(len(event_list))
        selected = event_list[index]
        print(f"Got event from list: {selected}")
        event_list[:] = event_list[:index] + event_list[index + 1:]
        yield selected


def main() -> None:
    source = gen_event()
    for i in range(1000):
        player, action = next(source)
        print(f"Event {i}: Player {player} did action {action}")

    event_10: typing.List[tuple[str, str]] = []
    for _ in range(10):
        event_10 = event_10 + [next(source)]

    print(f"Built list of 10 events: {event_10}")

    for item in consume_event(event_10):
        print(f"Remains in list: {event_10}")


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    main()
