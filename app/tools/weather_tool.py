"""Weather tool placeholder."""
def get_weather_forecast(circuit: str) -> dict:
    """Return simulated weather conditions for a race circuit."""

    forecasts = {
        "silverstone": {
            "current_conditions": "dry",
            "rain_probability": 72,
            "rain_expected_in_minutes": 20,
            "track_temperature_c": 24,
            "air_temperature_c": 17,
        }
    }

    return forecasts.get(
        circuit.lower(),
        {"error": f"No weather data available for {circuit}"}
    )
