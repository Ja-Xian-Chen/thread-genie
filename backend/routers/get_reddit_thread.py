from fastapi import APIRouter
from schemas.get_reddit_thread import threadRequest, threadResponse
from core.get_reddit_thread import get_reddit_thread

router = APIRouter()


@router.post("/", response_model=threadResponse)
async def get_reddit_thread_response(payload: threadRequest):
    thread = await get_reddit_thread(payload.question, payload.subreddit)
    return {"thread": thread}
