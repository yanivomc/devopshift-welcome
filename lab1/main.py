valid_server = {"nginx", "docker", "apache"}
try:
    server = input("Enter a server name: ")
    if server == "":
        raise ValueError("Server name is empty.")
    if not server.isalnum():
        raise ValueError("Server name must be alphanumeric.")
    if server not in valid_server:
        raise ValueError("Server is not recognized.")
    else:
        print("Server is running.")    
except ValueError as err:
    print(err)
    

     
