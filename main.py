from fastapi import FastAPI

app = FastAPI()


# This way we can create an API
@app.get('/')
def index():
    return {'data': {'name': 'Himanshu'}}  # 'Hi Himanshu'


@app.get('/about')
def about():
    return {'data': 'about page'}
