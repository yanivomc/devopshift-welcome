# Solution: Understanding Python Objects and Memory (DevOps Mock Lab)

# 1. Setting Up Variables and Memory References
servers = ["server1", "server2", "server3"]  # Original list of servers
active_servers = servers  # Both variables point to the same list

# Adding a new server to active_servers
active_servers.append("server4")
print("Servers:", servers)  # Output: ["server1", "server2", "server3", "server4"]
print("Active Servers:", active_servers)  # Same as servers

# Checking memory addresses
print("Memory address of servers:", id(servers))
print("Memory address of active_servers:", id(active_servers))

# Key Observation: Both variables share the same memory address, showing they reference the same object.

# 2. Managing Immutable Types
server_ip = "192.168.1.1"
server_endpoint = server_ip + ":80"  # Creating a new string object
print("Server IP:", server_ip)  # Output: "192.168.1.1"
print("Server Endpoint:", server_endpoint)  # Output: "192.168.1.1:80"

# Checking memory addresses
print("Memory address of server_ip:", id(server_ip))
print("Memory address of server_endpoint:", id(server_endpoint))

# Key Observation: Strings are immutable; a new object is created for server_endpoint.

# 3. Using Mutable Types
server_roles = {"server1": "web", "server2": "db", "server3": "cache"}
all_roles = server_roles  # Both variables point to the same dictionary

# Adding a new role
all_roles["server4"] = "monitoring"
print("Server Roles:", server_roles)  # Changes reflect in server_roles

# Key Observation: Dictionaries are mutable; changes in one reference affect the other.

# Creating a copy to avoid unintended changes
safe_roles = server_roles.copy()
safe_roles["server1"] = "proxy"
print("Server Roles:", server_roles)  # Original remains unchanged
print("Safe Roles:", safe_roles)  # Modified copy

# 4. Immutable vs. Mutable in a Function
def update_server_list(servers):
    servers.append("new_server")

servers = ["server1", "server2"]
print("Before update:", servers)
update_server_list(servers)
print("After update:", servers)  # Original list is modified

# Key Observation: Passing a mutable object to a function allows it to be modified directly.

# Bonus Challenge
def assign_roles(server_list, role):
    new_roles = server_list[:]  # Create a copy of the list
    return {server: role for server in new_roles}

servers = ["server1", "server2", "server3"]
roles = assign_roles(servers, "web")
print("Original Servers:", servers)  # Remains unchanged
print("Assigned Roles:", roles)  # New dictionary with assigned roles
