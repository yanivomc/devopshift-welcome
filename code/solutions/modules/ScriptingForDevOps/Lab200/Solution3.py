# Task 3: Generating a Configuration File
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

try:
    with open("app_config.json", "w") as file:
        file.write(str(config))
    print("Configuration file generated: app_config.json")
except Exception as e:
    print(f"An error occurred: {e}")