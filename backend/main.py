
from datetime import datetime
from typing import Optional, Text
from fastapi import FastAPI
from pydantic import BaseModel


from uuid import uuid4 as uuid



app = FastAPI()

class Post(BaseModel):
    id: Optional[str] = str(uuid())
    title:str
    author:str
    content: Text
    created_at:datetime = datetime.now()
    published: bool = False

posts = []
@app.get("/")
async def root():
    return {"message": "Hello Cris"}


@app.get("/posts")
async def get_posts():
    return posts

@app.post("/posts")
async def save_post(post:Post):
    # post.id = str(uuid())
    print(post.model_dump())
    posts.append(post.model_dump())
    return "recibido"