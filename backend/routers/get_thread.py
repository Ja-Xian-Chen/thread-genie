from fastapi import APIRouter
from schemas.get_thread import threadRequest, threadResponse
from core.get_thread import get_thread

router = APIRouter()


@router.post("/", response_model=threadResponse)
async def get_thread_response(payload: threadRequest):
    thread = await get_thread(payload.question, payload.subreddit)
    return {"thread": thread}
