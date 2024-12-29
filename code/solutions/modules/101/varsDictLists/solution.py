# Solution for Task 1: Collect Server Information
servers = []  # Create an empty list to store server names

# Prompt the user to enter the names of three servers
for i in range(1, 4):
    server_name = input(f"Enter the name of server {i}: ").strip()
    servers.append(server_name)

# Print the list of servers
print(f"Servers: {servers}")

# Solution for Task 2: Assign IP Addresses to Servers
server_configurations = {}  # Create an empty dictionary for server configurations

# Prompt the user to enter an IP address for each server
for server in servers:
    ip_address = input(f"Enter the IP address for {server}: ").strip()
    server_configurations[server] = ip_address

# Print the dictionary of server configurations
print(f"Server configurations: {server_configurations}")

# Solution for Task 3: Display Server Details
# Prompt the user to enter a server name to view its details
server_to_check = input("Enter a server name to view details: ").strip()

# Check if the server exists in the dictionary
if server_to_check in server_configurations:
    print(f"{server_to_check} has IP address {server_configurations[server_to_check]}")
else:
    print(f"Error: {server_to_check} does not exist in the server configurations.")

# Solution for Task 4: Modify Server Configurations
# Ask the user if they want to update any server's IP address
update_ip = input("Do you want to update any server's IP address? (yes/no): ").strip().lower()

if update_ip == "yes":
    server_to_update = input("Enter the server name: ").strip()
    if server_to_update in server_configurations:
        new_ip = input(f"Enter the new IP address for {server_to_update}: ").strip()
        server_configurations[server_to_update] = new_ip
        print(f"Updated server configurations: {server_configurations}")
    else:
        print(f"Error: {server_to_update} does not exist in the server configurations.")
else:
    print("No updates were made.")
