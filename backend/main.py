
from datetime import datetime
from typing import Optional, Text
import uuid
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

class Post(BaseModel):
    id: Optional[str]
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
    post.id = str(uuid.uuid4())
    posts.append(post.model_dump())
    return posts[-1]

@app.get("/posts/{post_id}")
async def get_post(post_id:str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/posts/{post_id}")
async def delete_post(post_id:str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"message": "Post deleted successfully"}
    raise HTTPException(status_code=404, detail="Post not found")

@app.put("/posts/{post_id}")
async def update_post(post_id:str, Updated_post:Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["title"] = Updated_post.title
            posts[index]["author"] = Updated_post.author
            posts[index]["content"] = Updated_post.content
            return {"message": "Post updated successfully"}
    raise HTTPException(status_code=404, detail="Post not found")
