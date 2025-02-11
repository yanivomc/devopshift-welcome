from fastapi import FastAPI
import json
import httpx
app = FastAPI()

@app.get("/")
def hello_world():
    return "Hello World"

@app.get("/users")
def get_users():
    response = httpx.get('https://jsonplaceholder.typicode.com/users')
    return response.json()
