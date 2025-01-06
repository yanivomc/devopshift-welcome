# Simple Error Handling Lab
try:
    server_name = input("Enter server name: ").strip()

    # Validate input
    if not server_name or not server_name.isalnum():
        raise ValueError("Invalid server name.")

    # Check server status
    if server_name in ["nginx", "docker"]:
        print("Server is running.")
    else:
        print("Server not recognized.")

except ValueError as e:
    print(f"Error: {e}")