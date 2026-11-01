from google.adk.agents import Agent

strategy_reviewer_agent = Agent(
    name="strategy_reviewer",
    model="gemini-3.8-flash",
    description="Reviews strategy proposals for correctness and risk.",
    instruction="""
You review the proposed race strategy.

Check:
- pit lap timing
- tyre choice
- weather risk
- race-state fit
- whether the recommendation is internally consistent

Return one of:
PASS
or
FAIL with clear reasons and suggested improvements.
""",
)
