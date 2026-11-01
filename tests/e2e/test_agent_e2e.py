import os
import uuid

import pytest
from google.adk.runners import InMemoryRunner

from app.agent import app

pytestmark = pytest.mark.skipif(
    os.getenv("RUN_ADK_E2E") != "1",
    reason="Set RUN_ADK_E2E=1 to run live ADK end-to-end tests.",
)


async def _run_prompt(prompt: str) -> str:
    runner = InMemoryRunner(app=app)
    events = await runner.run_debug(
        prompt,
        user_id="e2e-user",
        session_id=f"e2e-{uuid.uuid4().hex}",
        quiet=True,
    )

    response_texts: list[str] = []
    for event in events:
        if getattr(event, "author", None) != "race_director":
            continue

        content = getattr(event, "content", None)
        if not content or not getattr(content, "parts", None):
            continue

        for part in content.parts:
            text = getattr(part, "text", None)
            if text:
                response_texts.append(text)

    return "\n".join(response_texts).strip()


@pytest.mark.asyncio
async def test_normal_user_prompt_returns_structured_strategy_response() -> None:
    response = await _run_prompt("Norris is P4 at Silverstone. Should we pit?")

    assert response
    assert "RECOMMENDATION" in response.upper()
    assert "CONFIDENCE" in response.upper()


@pytest.mark.asyncio
async def test_missing_information_requests_more_context() -> None:
    response = await _run_prompt("Should we pit?")

    assert response
    assert any(
        keyword in response.lower()
        for keyword in ("need", "more", "context", "missing", "unclear")
    )


@pytest.mark.asyncio
async def test_unsupported_driver_does_not_hallucinate_current_data() -> None:
    response = await _run_prompt("Analyse Ayrton Senna's current race.")

    assert response
    assert any(
        keyword in response.lower()
        for keyword in ("no race data", "unknown driver", "cannot", "missing")
    )
