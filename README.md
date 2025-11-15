# Personal AI Assistant (Reddit-Based)

This project is a **personal AI assistant** that answers questions based on real opinions from Reddit.  
Instead of guessing, it searches Reddit discussions, learns the common viewpoints, and then creates a helpful answer.

---

## How It Works (Simple Explanation)

1. **You ask a question** on the website.  
2. The backend **searches Reddit** for posts and comments related to your question.  
3. It sends what it finds to **an AI model**.  
4. The AI reads the Reddit opinions and creates a **summarized, balanced response**.  
5. You get an answer that reflects what real people think on Reddit.

---

## What the Project Uses (Plain English)

### **Website (Frontend)**
- Built with Next.js and Tailwind  
- Displays the chat interface where you type questions

### **Brain of the App (Backend)**
- Built with Python  
- Uses FastAPI to communicate between the website and the AI  
- Uses PRAW to read information from Reddit  
- Uses the OpenAI API to generate responses  
- Saves user inputs and AI outputs in a small database

---

## Why This Project Is Useful

- It gives **real-world opinions**, not generic AI text  
- You can ask about:
  - Product choices  
  - Career questions  
  - Relationship advice  
  - Tech opinions  
  - Lifestyle decisions  
- Responses are influenced by Reddit communities, not just AI training data

---

## Example Questions You Could Ask

- “What laptop do Reddit users recommend for programming?”  
- “Is New York good for young professionals?”  
- “What do Redditors think about remote work?”  

---

## Who This Is For

- Everyday users curious what Reddit thinks  
- People researching public opinions  
- Anyone wanting an AI assistant with a more **human, community-based voice**
