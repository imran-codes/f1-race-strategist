from app.tools.weather_tool import get_weather_forecast


def test_silverstone_weather():
    result = get_weather_forecast("silverstone")

    assert result["rain_probability"] == 72
    assert result["rain_expected_in_minutes"] == 20
    assert result["track_temperature_c"] == 24
    assert result["air_temperature_c"] == 17

