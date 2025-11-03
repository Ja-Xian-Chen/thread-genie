# Defines what your API expects and returns
from pydantic import BaseModel # BaseModel is a core class that helps with Validating data

# incoming requests to API requests
class threadRequest(BaseModel):
    input: str # user input data for API
    subreddit: str # allows for targeted data input

# response from API requests
class threadResponse(BaseModel):
    response: str
