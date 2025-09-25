from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import praw
import openai

app = FastAPI()  # Creates a FastAPI application instance, RUN WITH "uvicorn main:app --reload --port 8000"

# CORS = Cross-Origin Resource Sharing, by default, browsers block requests from a different origin (domain/port) for security.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Which domains are allowed (here: all)
    allow_credentials=True,    # Allow cookies / authentication headers
    allow_methods=["*"],       # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],       # Allow all headers (Authorization, Content-Type, etc.)
)
