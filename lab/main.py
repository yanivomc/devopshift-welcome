from fastapi import FastAPI
import json
import httpx
from dataclasses import dataclass
from datetime import datetime
import modules

app = FastAPI()
servers = modules.read_server_list()

@dataclass
class ServerStatusResponse:
    server_name: str
    server_status: str | bool

@app.get("/server")
def get_server(server_name: str) -> ServerStatusResponse:
    server_status = False
    for server in servers:
        if server.name == server_name:
            return ServerStatusResponse(server_name, server_status)
    return ServerStatusResponse(server_name, server_name + " Does not exist.")

 
@app.post("/server")
def add_server(server_name: str) -> ServerStatusResponse:
    modules.add_new_server(modules.Server(name=server_name, online=True, cpus=6, ram=10))
    return ServerStatusResponse(server_name, " Server was added and now is running.")
