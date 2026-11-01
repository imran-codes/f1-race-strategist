"""Analysis workflow."""

from google.adk.agents import LoopAgent, ParallelAgent, SequentialAgent

from ..agents.race_data_agent import race_data_agent
from ..agents.strategy_agent import strategy_agent
from ..agents.strategy_reviewer_agent import strategy_reviewer_agent
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
    max_iterations=3,
)

race_strategy_pipeline = SequentialAgent(
    name="race_strategy_pipeline",
    sub_agents=[
        parallel_analysis,
        strategy_review_loop,
    ],
)
