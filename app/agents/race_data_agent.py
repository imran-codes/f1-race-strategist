"""Race data agent placeholder."""
from google.adk.agents import Agent

from ..tools.race_data_tool import get_race_state

race_data_agent = Agent(
    name="race_data_specialist",
    model="gemini-3.8-flash",
    description="Retrieves and interprets the current race state.",
    instruction="""
You are an F1 race data specialist.

Retrieve race data when required.

Focus on:
- position
- lap
- gaps
- current tyre
- race progress

Return factual race information.

Do not invent unavailable race data.
""",
    tools=[get_race_state],
)
