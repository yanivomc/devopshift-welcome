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


# from log import setup_logging
# from invalid_server_error import InvalidServerError
# from valid_servers import valid_servers

# logger = setup_logging()

# def check_service_status(server_name):
#     try:
#         if server_name == "":
#             raise InvalidServerError("Server name is empty.")
#         if not server_name.isalnum():
#             raise InvalidServerError("Server name must be alphanumeric.")
#         if server_name not in valid_servers:
#             raise InvalidServerError("Server is not recognized.")
#         else:
#             return "Running"
#     except InvalidServerError:
#         raise ValueError
# if __name__ == "__main__":
#     server_name = ""
#     while server_name != "exit":
#             server_name = input("Enter a server name:\n")
#             server_name = server_name.strip().lower()
#             if server_name == "exit":
#                 break
#             try:
#                 status = check_service_status(server_name)
#                 logger.info("Valid Server name.")
#             except ValueError as err:
#                 logger.error("Invalid Server name.")


# import httpx
# import json
# from pprint import pprint

# response = httpx.get('https://jsonplaceholder.typicode.com/users')
# pprint(response)
# users = response.json()
# for user in users:
#     pprint(user['name'])
    