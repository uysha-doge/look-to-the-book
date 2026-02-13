from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_URL = 'sqlite:///db/pierre.db'
engine = create_engine(DB_URL, echo=True)

Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    

class Books(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title = mapped_column(String(35))
    ttl_pages = mapped_column(String(4))
    cur_pages = mapped_column(String(4))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

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
