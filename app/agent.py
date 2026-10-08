# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent
from google.adk.apps import App

from .agents.race_data_agent import race_data_agent
from .agents.strategy_agent import strategy_agent
from .agents.tyre_agent import tyre_agent
from .agents.weather_agent import weather_agent
from .workflows.analysis_workflow import parallel_analysis, race_strategy_pipeline

MODEL = "gemini-3.8-flash"


root_agent = Agent(
    name="race_director",
    model=MODEL,
    description="Coordinates specialist agents to produce F1 race strategy.",
    instruction="""
You are the Race Director for an AI Formula 1 strategy system.

Your job is to coordinate specialist agents.

Available specialists:

1. weather_specialist
2. tyre_specialist
3. race_data_specialist
4. strategy_specialist

Delegate specialist analysis when required.

Never invent race information.

For final strategy responses provide:

CURRENT SITUATION
RECOMMENDATION
WHY
RISKS
CONFIDENCE
""",
    sub_agents=[
        race_strategy_pipeline
    ],
)

app = App(
    root_agent=root_agent,
    name="F1-Race-Strategist",
)
