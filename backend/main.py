from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import get_reddit_thread  # imports Reddit routers
from core.get_reddit_thread import init_reddit, close_reddit # imports Reddit start/stop functions

# creates the FastAPI application
app = FastAPI(
    title="QThreads",
    description="An API to help get AI generated answers from online threads",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# allows for Cross Origin Resource Sharing with frontend domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# events when app starts
@app.on_event("startup")
async def startup_event():
    await init_reddit()

# events when app ends
@app.on_event("shutdown")
async def shutdown_event():
    await close_reddit()

# registers router for get_reddit_thread
app.include_router(get_reddit_thread.router,
    prefix="/answers", tags=["answers"]) # routes will appear in /answers in the FastAPI doc

# Runs app with Uvicorn and restarts server on code changes
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
