from fastapi import FastAPI
import json
import httpx
from dataclasses import dataclass
from datetime import datetime
from valid_servers import valid_servers

@dataclass
class ServerStatusResponse:
    server_name: str
    server_status: str | bool

app = FastAPI()

@app.get("/server")
def get_server(server_name: str) -> ServerStatusResponse:
    server_status = valid_servers.get(server_name, "Doest not exist.")
    return ServerStatusResponse(server_name, server_status)

 
@app.post("/server")
def add_server(server_name: str) -> ServerStatusResponse:
    valid_servers[server_name] = True
    return ServerStatusResponse(server_name, valid_servers[server_name])


# @dataclass
# class User:
#     name:str
#     email:str
#     date = datetime.now()


# @app.get("/")
# def hello_world():
#     return "Hello World"

# @app.get("/users")
# def get_users() ->list[User]:
#     response = httpx.get('https://jsonplaceholder.typicode.com/users')
#     return response.json()

# @app.post("/users")
# def create_user(new_user: User) -> bool:
#     return True