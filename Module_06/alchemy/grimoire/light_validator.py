def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed_ingredients: list[str] = light_spell_allowed_ingredients()
    value: list[str] = [x for x in allowed_ingredients if x in ingredients]
    is_valid: str = "VALID" if value else "INVALID"
    return f"{ingredients} - {is_valid}"
