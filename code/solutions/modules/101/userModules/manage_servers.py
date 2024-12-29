from server_utils import restart_service, calculate_uptime, check_service_status

# Restart a service
print(restart_service("nginx"))

# Calculate uptime
uptime = calculate_uptime(720, 1440)
print(f"Uptime: {uptime}%")

# Check service status
print(check_service_status("docker"))
print(check_service_status("apache"))
