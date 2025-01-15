# Task 1: Reading a Log File
import os
try:
    error_count = 0
    # Check what path the script is running from
    print("Current directory:", os.getcwd())
    # change the current directory to the location of our script as the script usually runs from the root directory of the project
    # the os.chdir() function is used to change the current working directory to the directory where the script is located
    # os.path.dirname(__file__) returns the directory where the script is located
    # __file__ is a special variable that contains the path to the current script
    os.chdir(os.path.dirname(__file__))
    with open("server.log", "r") as file:
        for line in file:
            print(line.strip())  # Remove extra whitespace
            if "ERROR" in line:
                error_count += 1
    print(f"Total ERROR entries: {error_count}")
except FileNotFoundError:
    print("Log file not found.")