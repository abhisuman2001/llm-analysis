from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

app = FastAPI()

# Logging setup to see errors in the dashboard
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# This must match the secret you put in the Google Form
MY_SECRET = "tds_secret_key" 

class QuizTask(BaseModel):
    email: str
    secret: str
    url: str

@app.get("/")
def home():
    return {"message": "Project is running!"}

@app.post("/solve")
def solve_quiz(task: QuizTask):
    logger.info(f"Received task: {task}")
    
    # 1. Verify Secret
    if task.secret != MY_SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    # 2. Placeholder Logic (We will add the AI part later)
    # For now, we just acknowledge receipt so the connection works.
    return {
        "message": "Task received. Logic coming soon.",
        "received_url": task.url
    }
