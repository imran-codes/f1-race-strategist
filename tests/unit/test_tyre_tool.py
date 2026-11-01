from app.tools.tyre_tool import analyse_tyre


def test_medium_tyre_with_18_laps_is_worn():
    result = analyse_tyre(
        compound="medium",
        tyre_age=18,
    )

    assert result["compound"] == "medium"
    assert result["age"] == 18
    assert result["estimated_laps_remaining"] == 10
    assert result["condition"] == "healthy"


def test_unknown_tyre_with_12_laps_is_worn():
    result = analyse_tyre(
        compound="unknown",
        tyre_age=12,
    )

    assert result == {'error': 'Unknown tyre compound'}

def test_old_soft_tyre_is_critical():
        result = analyse_tyre(
            compound="soft",
            tyre_age=17,
        )

        assert result["condition"] == "critical"
