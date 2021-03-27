from fastapi import FastAPI

app = FastAPI()


# This way we can create an API
@app.get('/')
def index():
    return {'data': {'name': 'Himanshu'}}  # 'Hi Himanshu'


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'unpublished'}


@app.get('/blog/{id}')
def show(id: int):  # if we don't use :int we will get string in the output
    # Fetch blog with id = '{id}'
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    # Fetch comments of blog with id = '{id}'
    return {'data': {'comment1', 'comment2', 'comment3'}}
