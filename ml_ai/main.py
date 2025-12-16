# # Starter ML/AI script
# import numpy as np
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier

# print('Hello, Machine Learning!')
# import os
# os.environ["OPENAI_API_KEY"] = ""
# 
# deepseek - ""
# os.environ["OPENROUTER_API_KEY"] = ""
# $env:OPENROUTER_API_KEY=""
#$env:GEMINI_API_KEY=""
# from google.genai.agents import LlmAgent
# from google.genai.tools import google_search
# from google.genai import web

# # Tool instance
# #google_search = google_search()

# # Agent definition
# dice_agent = LlmAgent(
#     model="gemini-2.0-flash-exp",
#     name="question_answer_agent",
#     description="A helpful assistant agent that can answer questions.",
#     instruction="""Respond to the query using google search""",
#     tools=[google_search],
# )

# # Launch the web UI
# web.run(dice_agent)




from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3-pro-preview",
    contents="India recent news Today?",
    config=config,
)

print(response.text)