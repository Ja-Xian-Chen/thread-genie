import asyncpraw
import os

from dotenv import load_dotenv

load_dotenv() # load the env data keys etc.

reddit = None  # will be initialized on startup

# initializes the reddit client and read credentials
# uses global reddit 
async def init_reddit():
    global reddit
    reddit = asyncpraw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent=os.getenv("USER_AGENT"),
        redirect_uri=os.getenv("REDIRECT_URI"),
    )

# makes sure that reddit closes safely avoids resource leaks
async def close_reddit():
    global reddit
    if reddit:
        await reddit.close()
        reddit = None


async def get_reddit_thread(question: str, subreddit: str) -> str: # takes in parameters for 

    # Fetches relevant Reddit comments from the given subreddit for context.
    global reddit
    try:
        sub = await reddit.subreddit(subreddit) # Access the subreddit 
        results = [] # stores results in dictionary
        async for submission in sub.search(question, limit=3): # searches the subreddit for posts and checks the submissions
            results.append({
                "title": submission.title,
                
                "selftext": submission.selftext[:500],  # limit text length
                "url": submission.url
            })
        return results
    except Exception as e: # return error if fails
        return f"Error fetching data from r/{subreddit}: {e}"
