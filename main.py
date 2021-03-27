from fastapi import FastAPI

app = FastAPI()


# This way we can create an API
@app.get('/')   # path operation decorator => @app
def index():    # path operation function => index
    return {'data': {'name': 'Himanshu'}}  # 'Hi Himanshu'


@app.get('/about')
def about():
    return {'data': 'about page'}
