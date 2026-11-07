#! /usr/bin/env python3


def secure_archive(
        filename: str,
        action: str = "r",
        content: str = "") -> tuple[bool, str]:
    if action == "w":
        try:
            with open(filename, "w") as file:
                file.write(content)
            return (True, 'Content successfully written to file')
        except Exception as e:
            return (False, str(e))
    elif action == "r":
        try:
            with open(filename, "r") as file:
                the_file = file.read()
            return (True, the_file)
        except Exception as e:
            return (False, str(e))
    return (False, f"Error: '{action}' is not a valid operation mode. \
Please use 'r' to read the file or 'w' to write to it.")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    file: tuple[bool, str] = secure_archive("text.txt", "r")
    print(file)
    print()
    if file[0]:
        print("Using 'secure_archive' to write \
previous content to a new file:")
        print(secure_archive("files.txt", "w", file[1]))


if __name__ == "__main__":
    main()
