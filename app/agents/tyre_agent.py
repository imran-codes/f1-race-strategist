"""Tyre agent placeholder."""
from google.adk.agents import Agent

from ..tools.tyre_tool import analyse_tyre


tyre_agent = Agent(
    name="tyre_specialist",
    model="gemini-3.8-flash",
    description="Analyses tyre condition and degradation.",
    instruction="""
You are an F1 tyre specialist.

Analyse tyre condition using the provided tyre analysis tool.

Focus on:
- tyre age
- estimated remaining life
- degradation risk
- pit urgency

Do not make the final race strategy decision.
""",
    tools=[analyse_tyre],
)