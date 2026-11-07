#! /usr/bin/env python3
import math


def get_player_pos() -> tuple[float | int, ...]:
    input_value = input("Enter new coordinates as floats in format 'x,y,z': ")
    if input_value.count(",") != 2:
        print("Invalid syntax")
        return get_player_pos()
    split_value = input_value.split(",")
    valid_tuple: tuple[float | int, ...] = ()
    for val in split_value:
        try:
            value = float(val)
            valid_tuple += (value,)
        except ValueError as e:
            print(f"Error on parameter '{val}':{e}")
            return get_player_pos()
    return valid_tuple


def main() -> None:
    print("Get a first set of coordinates")
    tuple_value = get_player_pos()
    x1, y1, z1 = tuple_value[0], tuple_value[1], tuple_value[2]
    print(f"Got a first tuple: {tuple_value}")
    print(f"It include: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {round(math.sqrt(x1**2 + y1**2 + z1**2), 4)}")
    print()
    print("Get a second set of coordinates")
    tuple_value = get_player_pos()
    x2, y2, z2 = tuple_value[0], tuple_value[1], tuple_value[2]
    print(f"Distance between the 2 sets of coordinates: \
{round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2), 4)}")


if __name__ == "__main__":
    try:
        print("=== Game Coordinate System ===")
        main()
    except KeyboardInterrupt as e:
        print(e)
