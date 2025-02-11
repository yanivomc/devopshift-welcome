from pydantic import BaseModel, ValidationError
import json


class ServerStatusResponse(BaseModel):
    server_name: str
    server_status: str | bool


class Server(BaseModel):
    name: str
    online: bool
    cpus: int
    ram: int


def read_server_list() -> list[Server]:
    with open("servers.txt", "r") as f:
        servers: list[Server] = []
        for line in f.readlines():
            if line.strip():
                json_object = json.loads(line)
                try:
                    new_server = Server(**json_object)
                except ValidationError:
                    pass
                else:
                    servers.append(new_server)
    return servers


def add_new_server(new_server: Server):
    with open("servers.txt", "a") as f:
        f.write("\n")
        f.write(new_server.model_dump_json())
        

print(read_server_list())