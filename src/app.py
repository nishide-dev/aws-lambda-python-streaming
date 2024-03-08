# external imports
import os
import sys
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import uvicorn

# internal imports
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(ROOT_DIR)
from src.lib.types import RequestBody
from config.env import OPENAI_API_KEY, OPENAI_CHAT_MODEL

# define the app
app = FastAPI()


# openai chat
def openai_stream(prompt):
    chat = ChatOpenAI(
        model=OPENAI_CHAT_MODEL,
        api_key=OPENAI_API_KEY,
    )
    chain = chat | StrOutputParser()
    for chunk in chain.stream(prompt):
        yield chunk


# define the route
@app.post("/api/llm")
async def api_llm(body: RequestBody):
    return StreamingResponse(
        openai_stream(body.prompt),
        media_type="text/event-stream",
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
