from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = dark_spell_allowed_ingredients()
    value: list[str] = [x for x in allowed_ingredients if x in ingredients]
    is_valid: str = "VALID" if value else "INVALID"
    return f"{ingredients} - {is_valid}"
