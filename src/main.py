# Entry point for running the FastAPI app
from src.agent.api import app as api_app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api_app, host="0.0.0.0", port=8000)
