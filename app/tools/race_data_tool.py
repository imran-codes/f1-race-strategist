"""Race data tool placeholder."""
def get_race_state(driver: str) -> dict:
    """Return the current race state for a driver."""

    race_state = {
        "norris": {
            "driver": "Lando Norris",
            "position": 4,
            "lap": 31,
            "total_laps": 52,
            "tyre_compound": "medium",
            "tyre_age": 18,
            "gap_ahead_seconds": 2.7,
            "gap_behind_seconds": 3.4,
        },
    }

    return race_state.get(
        driver.lower(),
        {"error": f"No race data found for {driver}"}
    )