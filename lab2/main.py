from log import setup_logging
from invalid_server_error import InvalidServerError
from valid_servers import valid_servers

logger = setup_logging()

def check_service_status(server_name):
    try:
        if server_name == "":
            raise InvalidServerError("Server name is empty.")
        if not server_name.isalnum():
            raise InvalidServerError("Server name must be alphanumeric.")
        if server_name not in valid_servers:
            raise InvalidServerError("Server is not recognized.")
        else:
            return "Runing"
    except InvalidServerError:
        raise ValueError
if __name__ == "__main__":
    server_name = ""
    while server_name != "exit":
            server_name = input("Enter a server name:\n")
            server_name = server_name.strip().lower()
            if server_name == "exit":
                break
            try:
                status = check_service_status(server_name)
                logger.info("Valid Server name.")
            except ValueError as err:
                logger.error("Invalid Server name.")
