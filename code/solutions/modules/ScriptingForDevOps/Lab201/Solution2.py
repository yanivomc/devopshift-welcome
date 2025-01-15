import subprocess

service_name = "nginx"

try:
    # Check service status
    result = subprocess.run(["systemctl", "status", service_name], capture_output=True, text=True)

    if result.returncode == 0:
        print(f"Service {service_name} is running.")
    else:
        print(f"Service {service_name} is not running.")

        # Restart the service
        restart_result = subprocess.run(["sudo", "systemctl", "restart", service_name], capture_output=True, text=True)

        if restart_result.returncode == 0:
            print(f"Service {service_name} restarted successfully.")
        else:
            print(f"Failed to restart {service_name}: {restart_result.stderr}")

except FileNotFoundError:
    print("Error: systemctl command not found.")
except PermissionError:
    print("Error: Permission denied. Try running the script with elevated privileges.")