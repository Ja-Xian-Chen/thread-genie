from pydantic import BaseModel


class threadRequest(BaseModel):
    input: str
    subreddit: str


class threadResponse(BaseModel):
    response: str
