import asyncpraw
import os

from dotenv import load_dotenv

load_dotenv()

reddit = None  # will be initialized on startup


async def init_reddit():
    global reddit
    reddit = asyncpraw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent=os.getenv("USER_AGENT"),
        redirect_uri=os.getenv("REDIRECT_URI"),
    )


async def close_reddit():
    global reddit
    if reddit:
        await reddit.close()
        reddit = None


async def get_reddit_thread(question: str, subreddit: str) -> str:
    try:
        subreddit_obj = await reddit.subreddit(subreddit)

        # Fetch top 1 post
        submission = None
        async for post in subreddit_obj.top(time_filter="day", limit=1):
            submission = post
            break

        if not submission:
            return f"No posts found in r/{subreddit}"

        # Ensure comments are fetched asynchronously
        await submission.load()
        await submission.comments.replace_more(limit=0)

        top_comment = None
        for comment in submission.comments:
            if hasattr(comment, "body") and not getattr(comment, "stickied", False):
                top_comment = comment.body
                break

        return (
            f"Subreddit: r/{subreddit} "
            f"Title: {submission.title} "
            f"Top comment: {top_comment or 'No comments found'} "
        )

    except Exception as e:
        # for debugging you might want to log stacktrace here
        return f"Error fetching data from r/{subreddit}: {e}"
