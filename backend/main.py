from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import get_reddit_thread
from core.get_reddit_thread import init_reddit, close_reddit

app = FastAPI(
    title="QThreads",
    description="An API to help get AI generated answers from online threads",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# startup / shutdown events

@app.on_event("startup")
async def startup_event():
    await init_reddit()


@app.on_event("shutdown")
async def shutdown_event():
    await close_reddit()

app.include_router(get_reddit_thread.router,
    prefix="/answers", tags=["answers"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
