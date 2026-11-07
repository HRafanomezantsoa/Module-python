#! /usr/bin/env python3
import sys
import typing


def ft_archive_creation() -> None:
    if len(sys.argv) == 2:
        try:
            print("=== Cyber Archives Recovery & Preservation ===")
            print(f"Accessing file '{sys.argv[1]}'")
            file: typing.IO[str] = open(sys.argv[1])
            print("---\n")
            view = file.read()
            print(view)
            print("\n---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
            sharp = view.split('\n')
            lines = []
            for line in sharp:
                datas = line + '#\n'
                lines.append(datas)

            print("Transform data:")
            print("---\n")
            for data in lines:
                print(data, end='')
            print("\n---")
            sys.stdout.write("Enter a new file name (or empty): ", )
            sys.stdout.flush()
            new_file: str = sys.stdin.readline().strip()
            if new_file:
                try:
                    print(f"Saving data to '{new_file}'")
                    save: typing.IO[str] = open(new_file, "w")
                    for line in lines:
                        save.write(line)
                    print(f"Data saved in file '{new_file}'")
                except Exception as e:
                    sys.stderr.write(f"[STDERR] Error \
opening file '{new_file}': {e}\n")
                    print("Data not saved.")
                finally:
                    save.close()
            else:
                print("Not saving data.")
        except Exception as e:
            sys.stderr.write(f"[STDERR] Error \
opening file '{sys.argv[1]}': {e}\n")
    else:
        print(f"Usage: {sys.argv[0]} <file>")


if __name__ == "__main__":
    try:
        ft_archive_creation()
    except KeyboardInterrupt as e:
        print(e)
