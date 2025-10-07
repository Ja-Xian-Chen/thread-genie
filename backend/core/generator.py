# core/generator.py
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_KEY"))


async def generator(question: str, subreddit: str, reddit_data) -> str:
    """
    Generate a helpful AI response using Reddit discussion context.
    """
    context_text = ""
    if isinstance(reddit_data, list):
        for post in reddit_data:
            context_text += f"- {post['title']}: {post['selftext']}\n"
    else:
        context_text = str(reddit_data)

    prompt = (
        f"You are browsing r/{subreddit}. "
        f"Someone asked: '{question}'.\n\n"
        f"Here are some related Reddit posts:\n{context_text}\n\n"
        f"Write a natural, helpful, Reddit-style response summarizing the best advice."
    )

    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful Reddit-style assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error generating AI response: {e}"
