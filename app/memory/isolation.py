# Session A
#
# Driver: Norris
#
# Circuit: Silverstone
#
# Position: P4
#
#
# Session B
#
# Driver: Leclerc
#
# Circuit: Monza
#
# Position: P2


import asyncio

from google.adk.sessions import InMemorySessionService


async def main():
    service = InMemorySessionService()

    session_a = await service.create_session(
        app_name="f1_race_strategist",
        user_id="demo_user",
        state={
            "driver": "Norris",
            "circuit": "Silverstone",
        },
    )

    session_b = await service.create_session(
        app_name="f1_race_strategist",
        user_id="demo_user",
        state={
            "driver": "Leclerc",
            "circuit": "Monza",
        },
    )

    saved_a = await service.get_session(
        app_name="f1_race_strategist",
        user_id="demo_user",
        session_id=session_a.id,
    )

    saved_b = await service.get_session(
        app_name="f1_race_strategist",
        user_id="demo_user",
        session_id=session_b.id,
    )

    print("Session A:", saved_a.state)
    print("Session B:", saved_b.state)

    assert saved_a.id != saved_b.id
    assert saved_a.state["driver"] == "Norris"
    assert saved_b.state["driver"] == "Leclerc"


if __name__ == "__main__":
    asyncio.run(main())
