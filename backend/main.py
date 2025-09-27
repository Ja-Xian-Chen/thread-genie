from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title ="Reddit Libarian",
    description="api to help get answers from reddit",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
    