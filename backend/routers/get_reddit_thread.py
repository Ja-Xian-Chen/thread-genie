from fastapi import APIRouter # APIrouter allows for endpoints to be groupand reused
from schemas.get_reddit_thread import threadRequest, threadResponse # imports the models from schemas
from core.get_reddit_thread import get_reddit_thread # importing a function from core that handles getting data from reddit
from core.generator import generator # imports function from that generates response from AI

router = APIRouter() # new router instance 


@router.post("/", response_model=threadResponse) # Defines a POST endpoint at "/input"
async def get_reddit_thread_response(payload: threadRequest):
    # get Reddit  by calling reddit function
    reddit_data = await get_reddit_thread(payload.input, payload.subreddit)

    # generate AI response using Reddit context by calling gnerator function
    ai_response = await generator(payload.input, payload.subreddit, reddit_data)

    # returns the AI response
    return {"response": ai_response}
