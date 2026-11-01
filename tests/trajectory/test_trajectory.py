from google.adk.agents import LoopAgent, ParallelAgent, SequentialAgent

from app.agent import root_agent


def test_strategy_trajectory_shape() -> None:
    """Verify the agent graph follows the intended workflow trajectory."""
    assert len(root_agent.sub_agents) == 1

    pipeline = root_agent.sub_agents[0]
    assert isinstance(pipeline, SequentialAgent)
    assert pipeline.name == "race_strategy_pipeline"
    assert len(pipeline.sub_agents) == 2

    parallel_analysis = pipeline.sub_agents[0]
    strategy_review_loop = pipeline.sub_agents[1]

    assert isinstance(parallel_analysis, ParallelAgent)
    assert parallel_analysis.name == "parallel_race_analysis"
    assert {agent.name for agent in parallel_analysis.sub_agents} == {
        "weather_specialist",
        "tyre_specialist",
        "race_data_specialist",
    }

    assert isinstance(strategy_review_loop, LoopAgent)
    assert strategy_review_loop.name == "strategy_review_loop"
    assert strategy_review_loop.max_iterations == 3
    assert [agent.name for agent in strategy_review_loop.sub_agents] == [
        "strategy_specialist",
        "strategy_reviewer",
    ]
