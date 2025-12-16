# # Starter ML/AI script
# import numpy as np
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier

# print('Hello, Machine Learning!')
# import os
# os.environ["OPENAI_API_KEY"] = "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"
# #API KEY openai ="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"
# "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"
# deepseek - sk-37e7947a7ce24108a32544627189fae8
# os.environ["OPENROUTER_API_KEY"] = "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"
# $env:OPENROUTER_API_KEY="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"
#$env:GEMINI_API_KEY="AIzaSyAHVn38axA72PBxTSqT2klHPhFCl_Z6mpE"
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