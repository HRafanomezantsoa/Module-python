from alchemy.potions import strength_potion
from elements import create_fire
from ..elements import create_air


def lead_to_gold() -> str:
    return f"Recipe transmuting lead to Gold: brew '{create_air()}' \
and '{strength_potion()}' mixed with '{create_fire()}'"
