#! /usr/bin/env python3
import sys


def ft_command_quest() -> None:
    print(f"Program name: {sys.argv[0]}")
    length = len(sys.argv)
    if length == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {length - 1}")
        i = 1
        for argument in sys.argv[1:]:
            print(f"Argument {i}: {argument}")
            i += 1
    print(f"Total arguments: {length}\n")


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest()
