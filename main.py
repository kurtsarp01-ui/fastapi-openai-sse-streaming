import os
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="FastAPI OpenAI Streaming Cheatsheet")

app.add_middleware(
    CORSMiddleware,
    allow_origing=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#OpenAI Async Client Initialization
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY" , "your-api-key-here"))

@app.get("/stream")
async def stream_openai_response(prompt: str):
    """
    Endpoint providing live letters with Server-Sent Events(SSE).
    """
    async def event_generator():
        try:
            response = await client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            )

            async for chunk in response:
                content = chunk.choices[0].delta.content or ""
                if content:
                    yield {"data": content}
                    await asyncio.sleep(0.01)

        except Exception as e:
            yield {"data": f"[ERROR]: {str(e)}"}

    return EventSourceResponse(event_generator())
     