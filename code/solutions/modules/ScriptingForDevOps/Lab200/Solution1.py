import subprocess

try:
    # List files in /var/log
    result = subprocess.run(["ls", "-l", "/var/log"], capture_output=True, text=True)

    if result.returncode == 0:
        print(result.stdout)  # Print the output if the command succeeds
    else:
        print(f"Error: {result.stderr}")

except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: Permission denied.")