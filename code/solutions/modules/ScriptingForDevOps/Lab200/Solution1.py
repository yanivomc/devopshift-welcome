# Task 1: Reading a Log File
try:
    error_count = 0
    with open("server.log", "r") as file:
        for line in file:
            print(line.strip())  # Remove extra whitespace
            if "ERROR" in line:
                error_count += 1
    print(f"Total ERROR entries: {error_count}")
except FileNotFoundError:
    print("Log file not found.")