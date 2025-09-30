from fastapi import APIRouter
from schemas.answer import AnswerRequest, AnswerResponse
from core.answer_generator import generate_summary

router = APIRouter()


@router.post("/", response_model=AnswerResponse)
async def get_answer(payload: AnswerRequest):
    summary = await generate_summary(payload.question, payload.subreddit)
    return {"summary": summary}
