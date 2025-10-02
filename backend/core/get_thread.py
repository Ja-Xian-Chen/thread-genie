import praw
import os
from dotenv import load_dotenv

# Load env (works both with uv and plain python)
load_dotenv()

# Initialize praw once
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT"),
    redirect_uri=os.getenv("REDIRECT_URI"),
)


async def get_thread(question: str, subreddit: str) -> str:
    """Fetch the top post + top comment from a subreddit and return a thread string."""

    try:
        # Get top 1 post of the day
        submission = next(reddit.subreddit(
            subreddit).top(time_filter="day", limit=1))

        # Get top 1 comment (excluding stickied ones)
        top_comment = None
        for comment in submission.comments:
            if hasattr(comment, "body") and not comment.stickied:
                top_comment = comment.body
                break

        return (
            # f"Question: {question}\n\n"
            f"Subreddit: r/{subreddit}"
            f" Title: {submission.title}"
            # f"- Score: {submission.score}\n"
            # f"- URL: {submission.url}\n\n"
            f" Top comment: {top_comment or 'No comments found'}"
        )
    except Exception as e:
        return f"Error fetching data from r/{subreddit}: {e}"
