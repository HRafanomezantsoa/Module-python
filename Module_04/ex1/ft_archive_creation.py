#! /usr/bin/env python3
import sys
import typing


def ft_archive_creation() -> None:
    if len(sys.argv) == 2:
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file: typing.IO[str] = open(sys.argv[1])
            print("---\n")
            view = file.read()
            print(view)
            print("\n---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
            lines = []
            if view != "":
                sharp = view.split('\n')
                for line in sharp:
                    datas = line + '#\n'
                    lines.append(datas)
            print("Transform data:")
            print("---\n")
            for data in lines:
                print(data, end='')
            print("\n---")
            new_file: str = input("Enter a new file name (or empty): ")
            if new_file:
                print(f"Saving data to '{new_file}'")
                save: typing.IO[str] = open(new_file, "w")
                for line in lines:
                    save.write(line)
                print(f"Data saved in file '{new_file}'")
            else:
                print("Not saving data.")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        finally:
            save.close()
    else:
        print(f"Usage: {sys.argv[0]} <file>")


if __name__ == "__main__":
    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        ft_archive_creation()
    except KeyboardInterrupt as e:
        print(e)
