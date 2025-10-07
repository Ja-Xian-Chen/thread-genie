from fastapi import APIRouter
from schemas.get_reddit_thread import threadRequest, threadResponse
from core.get_reddit_thread import get_reddit_thread
from core.generator import generator

router = APIRouter()


@router.post("/", response_model=threadResponse)
async def get_reddit_thread_response(payload: threadRequest):
    # Step 1: get Reddit data
    reddit_data = await get_reddit_thread(payload.input, payload.subreddit)

    # Step 2: generate AI response using Reddit context
    ai_response = await generator(payload.input, payload.subreddit, reddit_data)

    return {"response": ai_response}
