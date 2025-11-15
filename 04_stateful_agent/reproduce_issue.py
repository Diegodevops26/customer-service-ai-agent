import asyncio
import sys
import os

# Add the current directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from google.adk.agents import Agent
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions import Session, InMemorySessionService
from agent import root_agent

async def reproduce_error():
    print(f"\n🚀 Running reproduction script for agent: '{root_agent.name}'...")
    
    session_service = InMemorySessionService()
    user_id = "test_user"
    
    # Create session WITHOUT initial state, simulating adk web behavior
    session = await session_service.create_session(
        app_name=root_agent.name,
        user_id=user_id,
        # state={} # Intentionally empty or None
    )
    
    query = "I'm in Kyoto. Plan a morning activity for me."
    
    runner = Runner(
        agent=root_agent,
        session_service=session_service,
        app_name=root_agent.name
    )
    
    try:
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session.id,
            new_message=types.Content(parts=[types.Part(text=query)], role="user")
        ):
            pass
        print("✅ Execution completed (Unexpected if error should occur)")
    except Exception as e:
        print(f"\n✅ Caught expected error: {type(e).__name__}: {e}")

if __name__ == "__main__":
    asyncio.run(reproduce_error())
