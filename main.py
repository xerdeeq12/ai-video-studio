
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="AI Video Studio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://xerdeeq12.github.io"
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class VideoRequest(BaseModel):
    prompt: str
    category: str = "Other"

@app.get("/")
def home():
    return {
        "message": "AI Video Studio API is running!",
        "status": "ready"
    }

@app.post("/generate")
def generate_video(request: VideoRequest):
    prompt = request.prompt.strip()

    if not prompt:
        return {"error": "Please enter a video idea."}

    return {
        "status": "prototype",
        "message": "Your video brief has been received. AI generation is not connected yet.",
        "prompt": prompt,
        "category": request.category
    }
