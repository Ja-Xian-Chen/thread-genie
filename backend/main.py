from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import praw
import openai

app = FastAPI()

