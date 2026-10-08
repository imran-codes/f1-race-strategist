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

from app.agent import app, get_current_time, get_the_weather, root_agent


def test_agent_module_wires_expected_symbols() -> None:
    assert root_agent.name == "f1_race_strategist"
    assert app.name == "app"


def test_agent_helpers_produce_expected_output() -> None:
    assert get_the_weather("San Francisco") == "It's 60 degrees and foggy."
    assert "current time" in get_current_time("San Francisco")
