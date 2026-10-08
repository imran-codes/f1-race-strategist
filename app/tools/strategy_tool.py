"""Strategy tool placeholder."""
def calculate_pit_window(
    current_lap: int,
    tyre_age: int,
    rain_expected_in_minutes: int | None = None,
) -> dict:
    """Calculate a simple candidate pit window."""

    suggested_lap = current_lap + 3

    if tyre_age >= 18:
        suggested_lap = current_lap + 2

    if rain_expected_in_minutes is not None:
        if rain_expected_in_minutes <= 10:
            suggested_lap = current_lap + 1

    return {
        "earliest_pit_lap": current_lap + 1,
        "suggested_pit_lap": suggested_lap,
        "reason": "Calculated from tyre age and weather risk.",
    }