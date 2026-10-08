"""Weather agent placeholder."""
from google.adk.agents import Agent

from ..tools.weather_tool import get_weather_forecast


weather_agent = Agent(
    name="weather_specialist",
    model="gemini-3.8-flash",
    description="Analyses weather conditions affecting race strategy.",
    instruction="""
You are an F1 weather strategist.

Your responsibility is ONLY weather analysis.

Use the weather tool whenever weather information is required.

Explain:
- current conditions
- rain probability
- expected weather changes
- strategic implications

Do not decide the final race strategy.
""",
    tools=[get_weather_forecast],
)