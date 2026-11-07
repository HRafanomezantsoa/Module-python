#! /usr/bin/env python3
import sys
import typing


def ft_ancient_test() -> None:
    if len(sys.argv) == 2:
        print("=== Cyber Archives Recovery ===")
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file: typing.IO[str] = open(sys.argv[1], "r")
            print("---\n")
            view = file.read()
            print(view)
            print("\n---")
            print(f"File '{sys.argv[1]}' closed.")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        finally:
            file.close()
    else:
        print(f"Usage: {sys.argv[0]} <file>")


if __name__ == "__main__":
    ft_ancient_test()
