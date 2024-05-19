# app/main.py

from fastapi import FastAPI
from app.routes.kibana import router as kibana_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add the origin(s) of your frontend application
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Add the allowed HTTP methods
    allow_headers=["Content-Type", "Authorization"],  # Add the allowed headers
)

app.include_router(kibana_router, prefix='/kibana')

@app.get('/')
def read_root():
    return {'message': 'Welcome to fastAPI Kibana service'}


@app.get('/hello')
def sayHello():
    return "Hello, How are you?"


# @app.post('/getdata')
# def getData():
