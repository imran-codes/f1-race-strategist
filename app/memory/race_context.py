

from google.adk.tools import ToolContext


def save_race_context(
    tool_context: ToolContext,
    driver: str | None = None,
    circuit: str | None = None,
    lap: int | None = None,
    position: int | None = None,
    tyre_compound: str | None = None,
    tyre_age: int | None = None,
) -> dict:
    """Save explicitly provided F1 race details to session state.

    Only pass fields that the user has provided.
    Do not infer or invent missing values.
    """

    updates = {
        "driver": driver,
        "circuit": circuit,
        "lap": lap,
        "position": position,
        "tyre_compound": tyre_compound,
        "tyre_age": tyre_age,
    }

    saved = {}

    for key, value in updates.items():
        if value is not None:
            tool_context.state[key] = value
            saved[key] = value

    return {
        "status": "success",
        "saved": saved,
    }


def get_race_context(tool_context: ToolContext) -> dict:
    """Retrieve saved F1 race context from this session."""

    fields = (
        "driver",
        "circuit",
        "lap",
        "position",
        "tyre_compound",
        "tyre_age",
    )

    context = {
        key: tool_context.state[key]
        for key in fields
        if key in tool_context.state
    }
    # When we use tool_context.state - ADK can track those changes as part of the execution's state updates. This is preferable to directly mutating a retrieved session object.

    return {
        "status": "success",
        "race_context": context,
    }
