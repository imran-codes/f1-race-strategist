
import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.agent import root_agent

APP_NAME = "f1_race_strategist"
USER_ID = "f1_demo_user"

session_service = InMemorySessionService()

runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service,
)


async def send_message(session_id: str, message: str) -> str:
    print(f"\nUSER: {message}")

    user_message = types.Content(
        role="user",
        parts=[types.Part(text=message)],
    )

    response_parts = []

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session_id,
        new_message=user_message,
    ):
        if event.is_final_response() and event.content:
            for part in event.content.parts or []:
                if part.text:
                    response_parts.append(part.text)

    response = "\n".join(response_parts)

    print(f"\nAGENT: {response}")
    return response


async def main():
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state={"race": "Silverstone"},
    )

    print(f"Created session: {session.id}")

    await send_message(
        session.id,
        "We are racing at Silverstone with Norris.",
    )

    await send_message(
        session.id,
        "He is P4 on lap 31 with 18-lap-old medium tyres.",
    )

    await send_message(
        session.id,
        "Rain is expected in 20 minutes. Should we pit?",
    )

    saved = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session.id,
    )

    print("\n--- SESSION INSPECTION ---")
    print("Session ID:", saved.id)
    print("State:", saved.state)
    print("Number of events:", len(saved.events))


if __name__ == "__main__":
    asyncio.run(main())
