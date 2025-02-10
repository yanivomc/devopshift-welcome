try:
    server = input("Enter a server name: ")
    if server == "":
        raise ValueError("Server name is empty.")
    if not server.isalnum():
        raise ValueError("Server name must be alphanumeric.")
except ValueError as err:
    print(err)
    

     
