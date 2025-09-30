from pydantic import BaseModel


class AnswerRequest(BaseModel):
    question: str
    subreddit: str


class AnswerResponse(BaseModel):
    summary: str
