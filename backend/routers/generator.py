from fastapi import APIRouter
from schemas.get_thread import threadRequest, threadResponse
from dotenv import load_dotenv
from core.generator import generator

router = APIRouter()
