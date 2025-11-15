import asyncio
import sys
import os

# Add the current directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from google.adk.agents import LlmAgent
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

def dynamic_instruction(*args, **kwargs):
    print(f"DEBUG: dynamic_instruction called with args={args}, kwargs={kwargs}")
    if len(args) > 0:
        print(f"DEBUG: arg[0] type: {type(args[0])}")
    if len(args) > 1:
        print(f"DEBUG: arg[1] type: {type(args[1])}")
    return "You are a helpful assistant."

async def test_callable_instruction():
    print(f"\n🚀 Running callable instruction test...")
    
    agent = LlmAgent(
        name="test_agent",
        model="gemini-2.5-flash",
        instruction=dynamic_instruction
    )
    
    session_service = InMemorySessionService()
    user_id = "test_user"
    session = await session_service.create_session(app_name=agent.name, user_id=user_id)
    
    runner = Runner(agent=agent, session_service=session_service, app_name=agent.name)
    
    try:
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session.id,
            new_message=types.Content(parts=[types.Part(text="Hello")], role="user")
        ):
            pass
        print("✅ Callable instruction worked!")
    except Exception as e:
        print(f"❌ Callable instruction failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_callable_instruction())
