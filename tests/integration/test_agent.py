from google.adk.agents import SequentialAgent

from app.agent import MODEL, app, root_agent


def test_agent_module_wires_expected_symbols() -> None:
    assert root_agent.name == "race_director"
    assert app.name == "F1-Race-Strategist"

def test_root_agent_is_registered() -> None:
    assert root_agent.name == "race_director"
    assert root_agent.model == MODEL


def test_root_agent_exposes_race_context_tools() -> None:
    assert {tool.__name__ for tool in root_agent.tools} == {
        "get_race_context",
        "save_race_context",
    }


def test_workflow_and_sub_agents_are_wired() -> None:
    # root_agent -> race_strategy_pipeline
    assert len(root_agent.sub_agents) == 1

    pipeline = root_agent.sub_agents[0]
    assert pipeline.name == "race_strategy_pipeline"

    # race_strategy_pipeline -> parallel_analysis, strategy_agent
    assert isinstance(pipeline, SequentialAgent)
    assert pipeline.name == "race_strategy_pipeline"
    assert len(pipeline.sub_agents) == 2

    assert pipeline.sub_agents[0].name == "parallel_race_analysis"
    assert pipeline.sub_agents[1].name == "strategy_review_loop"


    # parallel_analysis -> weather, tyre, race data
    parallel = pipeline.sub_agents[0]
    assert {agent.name for agent in parallel.sub_agents} == {
        "weather_specialist",
        "tyre_specialist",
        "race_data_specialist",
    }
