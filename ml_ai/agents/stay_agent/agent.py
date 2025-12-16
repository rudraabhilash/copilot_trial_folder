from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import json
import time

async def execute(request):
    stay_agent = Agent(
        name="stay_agent",
        model="gemini-2.5-flash-lite", #LiteLlm("openrouter/meta-llama/llama-3-70b-instruct"), # "openai/gpt-4o"
        description="Suggests hotel or stay options for a destination.",
        instruction=(
            "Given a destination, travel dates, and budget, suggest 2-3 hotel or stay options."
            "Include hotel name, location, price per night, and amenities. Ensure suggestions are within budget."
            "Respond in plain English. Keep it concise and well-formatted."
        )
    )
    USER_ID = "user_stay"
    SESSION_ID = "session_stay_001"
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name="stay_app",
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    time.sleep(5)  # Simulate some processing delay
    runner = Runner(
        agent=stay_agent,
        app_name="stay_app",
        session_service=session_service
    )
    prompt = (
        f"User is staying at {request['destination']} from {request['start_date']} to {request['end_date']}, "
        f"with a budget of {request['budget']}. Suggest 2-3 stay options."
        f"Include hotel name, location, price per night, and amenities. Keep it concise and well-formatted. "
    )
    message = types.Content(role="user", parts=[types.Part(text=prompt)])
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=message):
        if event.is_final_response():
            return {"stays": event.content.parts[0].text}
            # response_text = event.content.parts[0].text
            # try:
            #     parsed = json.loads(response_text)
            #     if "stays" in parsed and isinstance(parsed["stays"], list):
            #         return {"stays": parsed["stays"]}
            #     else:
            #         print("'stays' key missing or not a list in response JSON")
            #         return {"stays": response_text}  # fallback to raw text
            # except json.JSONDecodeError as e:
            #     print("JSON parsing failed:", e)
            #     print("Response content:", response_text)
            #     return {"stays": response_text}  # fallback to raw text