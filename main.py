from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# App name
app = FastAPI()


# This way we can create an API>
@app.get('/blog')  # /blog?limit=100&published=true
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished'}


@app.get('/blog/{id}')
def show(id: int):  # if we don't use :int we will get string in the output
    # Fetch blog with id = '{id}'
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int, limit: int = 10):
    # Fetch comments of blog with id = '{id}'
    return {'limit': limit}


# Model
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create(blog: Blog):
    return {'data': f"Blog is created with title as: {blog.title}"}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)
