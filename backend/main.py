from fastapi import FastAPI

app = FastAPI()

posts = []
@app.get("/")
async def root():
    return {"message": "Hello Cris"}


@app.get("/posts")
async def get_posts():
    return posts

