# core/generator.py
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_KEY")) # creates an async client using API key


async def generator(question: str, subreddit: str, reddit_data) -> str: # defines a function that takes in info
    context_text = "" # building a context string for GPT
    if isinstance(reddit_data, list): # if data is a list then we can combine top posts into one block
        for post in reddit_data:
            context_text += f"- {post['title']}: {post['selftext']}\n"
    else:
        context_text = str(reddit_data) # if not then convert to string

    # prompt below gives the full context to the GPT input
    prompt = (
        f"You are browsing r/{subreddit}. "
        f"Someone asked: '{question}'.\n\n"
        f"Here are some related Reddit posts:\n{context_text}\n\n"
        f"Write a natural, helpful, Reddit-style response summarizing the best advice."
    )
    # sends the completion request to OPENAI model
    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful Reddit-style assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content.strip() # Returns as clean strings

    except Exception as e: # return error if fail
        return f"Error generating AI response: {e}"
