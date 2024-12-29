# Task 1: Validate User Input
status = input("Enter server status (running, stopped, error): ").strip().lower()

if status == "running":
    print("The server is operational.")
elif status == "stopped":
    print("The server is down. Restart required.")
elif status == "error":
    print("The server is in an error state. Immediate action required!")
else:
    print("Invalid status entered.")

# Task 2: Monitor Multiple Servers
servers = ["server1", "server2", "server3"]

print("\nMonitoring servers...")
for server in servers:
    print(f"Pinging {server}...")
    print(f"Ping to {server} successful.")

# Task 3: Restart Servers in Error State
server_statuses = {
    "server1": "running",
    "server2": "error",
    "server3": "stopped"
}

print("\nChecking server statuses...")
for server, status in server_statuses.items():
    if status == "error":
        print(f"Restarting {server}...")
    elif status == "stopped":
        print(f"{server} is down. Restart required.")
    else:
        print(f"{server} is healthy.")

# Task 4: Automate Ping Requests
print("\nAutomated ping requests:")
while True:
    server_name = input("Enter a server name to ping (or type 'exit' to quit): ").strip()
    if server_name.lower() == "exit":
        print("Exiting ping automation...")
        break
    print(f"Pinging {server_name}... Ping successful.")
