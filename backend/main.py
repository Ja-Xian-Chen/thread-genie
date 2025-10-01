from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import answer
import praw
from dotenv import load_dotenv
import os

# Create the FastAPI application
app = FastAPI(
    title ="QThreads",
    description="An API to help get AI generated answers from online threads",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
# Setup middleware for Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load environment variables from a .env file
load_dotenv()


app.include_router(answer.router, prefix="/answers", tags=["answers"])

# uv run .\main.py
# when installing new packages use UV before the pip install
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0",port=8000, reload=True)