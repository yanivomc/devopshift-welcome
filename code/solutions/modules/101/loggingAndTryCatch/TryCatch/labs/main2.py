# Advanced Error Handling Lab

# Custom exception
class InvalidServerNameError(Exception):
    """Raised when the server name is invalid."""
    pass

def monitor_server(server_name):
    """Simulates server monitoring."""
    if server_name in ["nginx", "docker"]:
        return f"Server {server_name} is running."
    else:
        raise ValueError(f"{server_name} is not a recognized server.")

try:
    server_name = input("Enter server name: ").strip()

    # Validate input
    if not server_name or not server_name.isalnum():
        raise InvalidServerNameError("Invalid server name.")

    # Monitor server
    status = monitor_server(server_name)
    print(status)

except InvalidServerNameError as e:
    print(f"Error: {e}")

except ValueError as e:
    print(f"Error: {e}")