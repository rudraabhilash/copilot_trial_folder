# Python ML/AI & Web Development Workspace

This workspace is set up for machine learning, AI, and web development using Python. 

- ML/AI code: `ml_ai/main.py`
- Agent code: `ml_ai/agents/`
- Web app: `web_app/app.py`
- Requirements: `requirements.txt`

## Getting Started
1. Set up a Python virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Run ML/AI code: `python ml_ai/main.py`
4. Run web app: `python web_app/app.py`

#cd into ml_ai folder for sure else you will be in trouble!
#uvicorn agents.host_agent.__main__:app --port 8000 & 
#uvicorn agents.flight_agent.__main__:app --port 8001 & 
#uvicorn agents.stay_agent.__main__:app --port 8002 & 
#uvicorn agents.activities_agent.__main__:app --port 8003 & 
#streamlit run streamlit_app.py
