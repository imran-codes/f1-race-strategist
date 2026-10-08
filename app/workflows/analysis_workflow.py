"""Analysis workflow placeholder."""
from ..agents.strategy_agent import strategy_agent
from ..agents.strategy_reviewer_agent import strategy_reviewer_agent

# app/workflows/analysis_workflow.py
"""Analysis workflow."""

from google.adk.agents import ParallelAgent, SequentialAgent, LoopAgent

from ..agents.race_data_agent import race_data_agent
from ..agents.tyre_agent import tyre_agent
from ..agents.weather_agent import weather_agent

parallel_analysis = ParallelAgent(
    name="parallel_race_analysis",
    description="Analysis workflow for parallel agent",
    sub_agents=[
        weather_agent,
        tyre_agent,
        race_data_agent,
    ],
)

strategy_review_loop = LoopAgent(
    name="strategy_review_loop",
    sub_agents=[
        strategy_agent,
        strategy_reviewer_agent,
    ],
    # use the ADK version’s loop-control fields here
    # e.g. max_iterations / max_loops / timeout / cost guardrails
# max_iterations = 3
# time_limit = 20 seconds
# cost_limit = small fixed budget
# success_condition = reviewer returns PASS
)

race_strategy_pipeline = SequentialAgent(
    name="race_strategy_pipeline",
    sub_agents=[
        parallel_analysis,
        strategy_review_loop,
    ],
)