#! /usr/bin/env python3
import sys


def ft_score_analytics() -> None:
    scores: list = []
    invalid: list = []
    for i in sys.argv[1:]:
        try:
            value = int(i)
            scores += [value]
        except ValueError:
            invalid += [i]

    if not scores:
        if invalid:
            for i in invalid:
                print(f"Invalid parameter: '{i}'")
        print("No scores provided. Usage: python3\
 ft_score_analytics.py <score1> <score2> ...\n")
    else:
        print(f"Scores processed {scores}")
        print(f"Total players: {len(sys.argv) - 1}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}\n")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
