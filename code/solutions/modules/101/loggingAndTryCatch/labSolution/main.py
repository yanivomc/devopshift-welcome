import logging
import sys

# Custom exception
class InvalidServerNameError(Exception):
    """Raised when the server name is invalid."""
    pass

# Configure logging to stdout and stderr
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)  # Log all levels to stdout
    ]
)
stderr_handler = logging.StreamHandler(sys.stderr)  # Additional handler for critical errors
stderr_handler.setLevel(logging.ERROR)
logging.getLogger().addHandler(stderr_handler)

# Function to check server status
def check_service_status(server_name):
    """Simulates checking the status of a server."""
    if server_name in ["nginx", "docker"]:
        logging.info(f"Server {server_name} is running.")
        return "Running"
    else:
        raise ValueError(f"{server_name} is not a recognized server.")

# Main logic
try:
    server_name = input("Enter server name: ").strip()
    
    # Validate server name
    if not server_name or " " in server_name or not server_name.isalnum():
        raise InvalidServerNameError("Invalid server name.")
    
    # Check server status
    status = check_service_status(server_name)
    print(f"{server_name} status: {status}")

except InvalidServerNameError as e:
    logging.error(e)
    print(f"Error: {e}")

except ValueError as e:
    logging.error(e)
    print(f"Error: {e}")

except Exception as e:
    logging.critical(f"Critical Error: {e}")
    print(f"Critical Error: {e}")
