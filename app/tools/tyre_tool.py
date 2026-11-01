"""Tyre tool placeholder."""


def analyse_tyre(
    compound: str,
    tyre_age: int,
) -> dict:
    """Analyse tyre condition based on compound and age."""

    expected_life = {
        "soft": 18,
        "medium": 28,
        "hard": 38,
        "intermediate": 25,
        "wet": 30,
    }

    maximum_age = expected_life.get(compound.lower())

    if maximum_age is None:
        return {"error": "Unknown tyre compound"}

    life_remaining = maximum_age - tyre_age

    if life_remaining <= 3:
        condition = "critical"
    elif life_remaining <= 8:
        condition = "worn"
    else:
        condition = "healthy"

    return {
        "compound": compound,
        "age": tyre_age,
        "estimated_laps_remaining": max(life_remaining, 0),
        "condition": condition,
    }
