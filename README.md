# ⚡️ FastAPI + OpenAI SSE Streaming Starter Kit

A lightweight, non-blocking async FastAPI integration with OpenAI's Async API that streams ChatGPT-style responses live using **Server-Sent Events (SSE)**.

![FastAPI OpenAI SSE Streaming](https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/fastapi-openai-sse-streaming/main/cover.jpg)

---

## ✨ Features

- 📡 **Real-time SSE Streaming:** Live, word-by-word streaming using `sse-starlette`.
- ⚡️ **Async OpenAI Integration:** Built with the latest non-blocking `AsyncOpenAI` client.
- 🛠️ **Zero Configuration:** Simple 2-file architecture (`main.py` + `requirements.txt`).
- 🌐 **CORS Pre-configured:** Connects out of the box with React, Next.js, or Vue frontends.

---

## 🚀 Quick Start (Under 1 Minute)

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/fastapi-openai-sse-streaming.git](https://github.com/YOUR_GITHUB_USERNAME/fastapi-openai-sse-streaming.git)
cd fastapi-openai-sse-streaming

2. Install dependencies
pip install -r requirements.txt

3. Set your OpenAI API Key
Open main.py and replace sk-proj-YOUR_ACTUAL_OPENAI_API_KEY with your actual OpenAI key.

4. Run the server
python3 -m uvicorn main:app --reload

5. Test in browser
Navigate to:
http://127.0.0.1:8000/stream?prompt=Write%20a%20poem%20about%20coding
🛠️ Tech Stack
Framework: FastAPI
Server: Uvicorn
AI SDK: AsyncOpenAI (openai>=1.30.0)
Streaming: sse-starlette
🔥 Looking for a Production-Ready AI SaaS Boilerplate?
Need a full stack with user authentication, credit/usage limits, PostgreSQL database, and automated Stripe billing?
👉 [https://skassets.gumroad.com/l/cviylg]
📝 License
MIT License. Free to use in personal and commercial projects.
