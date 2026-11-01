
from types import SimpleNamespace

from app.memory.race_context import (
    get_race_context,
    save_race_context,
)


def test_save_race_context():
    context = SimpleNamespace(state={})

    result = save_race_context(
        tool_context=context,
        driver="Norris",
        circuit="Silverstone",
        lap=31,
        position=4,
    )

    assert result["status"] == "success"
    assert context.state["driver"] == "Norris"
    assert context.state["lap"] == 31
    assert context.state["position"] == 4


def test_get_race_context():
    context = SimpleNamespace(
        state={
            "driver": "Norris",
            "circuit": "Silverstone",
        }
    )

    result = get_race_context(
        tool_context=context,
    )

    assert result["race_context"]["driver"] == "Norris"
    assert result["race_context"]["circuit"] == "Silverstone"


def test_partial_update_preserves_other_fields():
    context = SimpleNamespace(
        state={
            "driver": "Norris",
            "lap": 30,
        }
    )

    save_race_context(
        tool_context=context,
        lap=31,
    )

    assert context.state["driver"] == "Norris"
    assert context.state["lap"] == 31
