from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


async def lifespan(app_: FastAPI):
    print("Bot is ready")
    yield

app = FastAPI(title="to do app", lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
async def glavstr():
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    return HTMLResponse(content=html_content)

