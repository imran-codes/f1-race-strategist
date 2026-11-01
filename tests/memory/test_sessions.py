
import pytest
from google.adk.sessions import InMemorySessionService

APP_NAME = "f1_race_strategist"
USER_ID = "test_user"


@pytest.mark.asyncio
async def test_create_session_with_initial_state():
    service = InMemorySessionService()

    session = await service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state={"driver": "Norris"},
    )

    assert session.id is not None
    assert session.state["driver"] == "Norris"


@pytest.mark.asyncio
async def test_session_can_be_retrieved():
    service = InMemorySessionService()

    created = await service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state={"circuit": "Silverstone"},
    )

    retrieved = await service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=created.id,
    )

    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.state["circuit"] == "Silverstone"


@pytest.mark.asyncio
async def test_sessions_are_isolated():
    service = InMemorySessionService()

    session_a = await service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state={"driver": "Norris"},
    )

    session_b = await service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state={"driver": "Leclerc"},
    )

    assert session_a.id != session_b.id

    retrieved_a = await service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session_a.id,
    )

    retrieved_b = await service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session_b.id,
    )

    assert retrieved_a.state["driver"] == "Norris"
    assert retrieved_b.state["driver"] == "Leclerc"


@pytest.mark.asyncio
async def test_in_memory_data_is_lost_with_new_service():
    original_service = InMemorySessionService()

    session = await original_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state={"driver": "Norris"},
    )

    restarted_service = InMemorySessionService()

    retrieved = await restarted_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session.id,
    )

    assert retrieved is None
