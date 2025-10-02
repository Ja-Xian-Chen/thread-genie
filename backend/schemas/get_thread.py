from pydantic import BaseModel


class threadRequest(BaseModel):
    question: str
    subreddit: str


class threadResponse(BaseModel):
    thread: str
