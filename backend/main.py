
from datetime import datetime
from typing import Optional, Text
import uuid
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException


# from uuid import uuid4



app = FastAPI()

class Post(BaseModel):
    id: Optional[str]
    title:str
    author:str
    content: Text
    # created_at:datetime = datetime.now()
    # published: bool = False

posts = []
@app.get("/")
async def root():
    return {"message": "Hello Cris"}


@app.get("/posts")
async def get_posts():
    return posts

@app.post("/posts")
async def save_post(post:Post):
    post.id = str(uuid.uuid4())
    print(post.id)
    print(post.model_dump())
    posts.append(post.model_dump())
    return posts[-1]

@app.get("/posts/{post_id}")
async def get_post(post_id:str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")
