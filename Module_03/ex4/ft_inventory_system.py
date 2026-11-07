#! /usr/bin/env python3
import sys


def ft_inventory_system() -> None:
    all_parameter: dict[str, int] = {}
    for i in sys.argv[1:]:
        if ":" not in i:
            print(f"Error - invalid parameter '{i}'")
            continue
        key, value = i.split(":", 1)
        if key in all_parameter.keys():
            print(f"Reduntant item '{key}' - discarding")
            continue
        try:
            int_value = int(value)
            all_parameter.update({key: int_value})
        except ValueError as e:
            print(f"Quantity error for '{key}' : {e}")
    print(f"Got inventory: {all_parameter}")
    print(f"Item list: {list(all_parameter.keys())}")
    print(f"Total quantity of the {len(all_parameter)} \
items: {sum(all_parameter.values())}")
    for key in all_parameter.keys():
        print(f"Item {key} represents\
 {round((all_parameter[key]/12)*100, 1)}%")
    keys = list(all_parameter.keys())
    if keys:
        item_most_k = keys[0]
        item_least_k = keys[0]
        item_most = all_parameter[item_most_k]
        item_least = all_parameter[item_least_k]
        for key in keys:
            if item_most < all_parameter[key]:
                item_most = all_parameter[key]
                item_most_k = key
            if item_least > all_parameter[key]:
                item_least = all_parameter[key]
                item_least_k = key
        print(f"Item most abundant: {item_most_k} with quantity {item_most}")
        print(f"Item least abundant:\
 {item_least_k} with quantity {item_least}")
        all_parameter.update({"magic_item": 1})
        print(f"Update inventory: {all_parameter}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    ft_inventory_system()
