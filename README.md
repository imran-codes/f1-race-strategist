# f1-race-strategist

Simple ReAct agent
Agent generated with `agents-cli` version `1.8.0`

## Project Structure

```
f1-race-strategist/
├── app/         # Core agent code
│   ├── agent.py               # Main agent logic
│   ├── fast_api_app.py        # FastAPI Backend server
│   └── app_utils/             # App utilities and helpers
├── tests/                     # Unit, integration, and load tests
├── GEMINI.md                  # AI-assisted development guide
└── pyproject.toml             # Project dependencies
```
app/
│
├── __init__.py
├── agent.py
│
├── agents/
│   ├── __init__.py
│   ├── weather_agent.py
│   ├── tyre_agent.py
│   ├── race_data_agent.py
│   └── strategy_agent.py
│
├── tools/
│   ├── __init__.py
│   ├── weather_tool.py
│   ├── tyre_tool.py
│   ├── race_data_tool.py
│   └── strategy_tool.py
│
└── workflows/
    ├── __init__.py
    ├── analysis_workflow.py
    └── strategy_loop.py
tests/
├── unit/
│   ├── test_weather_tool.py
│   ├── test_tyre_tool.py
│   └── test_strategy_tool.py
│
├── integration/
│   └── test_agent.py
│
└── eval/
    ├── datasets/
    │   └── f1-strategy-dataset.json
    └── eval_config.yaml

                 TOOLS

 Weather API logic
       ↑
 Weather Agent

 Tyre calculation
       ↑
 Tyre Agent

 Race state
       ↑
 Race Data Agent

 Pit calculation
       ↑
 Strategy Agent

////

Browser → exploratory testing

CLI → smoke testing

pytest → deterministic testing

evals → AI behaviour testing

> 💡 **Tip:** Use [Antigravity CLI](https://antigravity.google/) for AI-assisted development - project context is pre-configured in `GEMINI.md`.

## Requirements

Before you begin, ensure you have:
- **uv**: Python package manager (used for all dependency management in this project) - [Install](https://docs.astral.sh/uv/getting-started/installation/) ([add packages](https://docs.astral.sh/uv/concepts/dependencies/) with `uv add <package>`)
- **agents-cli**: Agents CLI - Install with `uv tool install google-agents-cli`
- **Google Cloud SDK**: For GCP services - [Install](https://cloud.google.com/sdk/docs/install)


## Quick Start

Install `agents-cli` and its skills if not already installed:

```bash
uvx google-agents-cli setup
```

Install required packages:

```bash
agents-cli install
```

Test the agent with a local web server:

```bash
agents-cli playground
```

You can also use features from the [ADK](https://adk.dev/) CLI with `uv run adk`.

## Commands

| Command              | Description                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------- |
| `agents-cli install` | Install dependencies using uv                                                         |
| `agents-cli playground` | Launch local development environment                                                  |
| `agents-cli lint`    | Run code quality checks                                                               |
| `agents-cli eval`    | Evaluate agent behavior (generate, grade, analyze, and more — see `agents-cli eval --help`) |
| `uv run pytest tests/unit tests/integration` | Run unit and integration tests                                                        || [A2A Inspector](https://github.com/a2aproject/a2a-inspector) | Launch A2A Protocol Inspector                                                        |

## 🛠️ Project Management

| Command | What It Does |
|---------|--------------|
| `agents-cli scaffold enhance` | Add CI/CD pipelines and Terraform infrastructure |
| `agents-cli infra cicd` | One-command setup of entire CI/CD pipeline + infrastructure |
| `agents-cli scaffold upgrade` | Auto-upgrade to latest version while preserving customizations |

---

## Development

Edit your agent logic in `app/agent.py` and test with `agents-cli playground` - it auto-reloads on save.

## Deployment

```bash
gcloud config set project <your-project-id>
agents-cli deploy
```

To add CI/CD and Terraform, run `agents-cli scaffold enhance`.
To set up your production infrastructure, run `agents-cli infra cicd`.

## Observability

Built-in telemetry exports to Cloud Trace, BigQuery, and Cloud Logging.

## A2A Inspector

This agent supports the [A2A Protocol](https://a2a-protocol.org/). Use the [A2A Inspector](https://github.com/a2aproject/a2a-inspector) to test interoperability.
See the [A2A Inspector docs](https://github.com/a2aproject/a2a-inspector) for details.
