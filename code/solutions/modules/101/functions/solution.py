# Sample Data
server_metrics = {
    "server1": [50, 70],
    "server2": [85, 90],
    "server3": [40, 60],
}

# Task 1: Analyze Server Data
def analyze_server(server_name, metrics):
    """
    Analyze metrics for a given server.
    Args:
        server_name (str): Name of the server.
        metrics (list): List of CPU and memory usage percentages.
    Returns:
        float: Average usage of the server.
    """
    if type(metrics) is not list:
        raise ValueError("Metrics should be a list.")

    total_usage = sum(metrics)
    num_metrics = len(metrics)
    average_usage = total_usage / num_metrics

    print(f"{server_name} - Total Usage: {total_usage}, Average Usage: {average_usage:.2f}%")
    return average_usage



# Task 2: Identify Over-Utilized Servers
def check_overutilized(servers, threshold=80):
    """
    Identify over-utilized servers.
    Args:
        servers (dict): Dictionary of server metrics.
        threshold (float): Utilization threshold percentage.
    Returns:
        list: List of over-utilized servers.
    """
    overutilized = []
    for server, metrics in servers.items():
        avg_usage = analyze_server(server, metrics)
        if avg_usage > threshold:
            overutilized.append(server)

    return overutilized


# Task 3: Report Overall Metrics
def generate_report(servers):
    """
    Generate a report of overall metrics.
    Args:
        servers (dict): Dictionary of server metrics.
    """
    total_cpu = 0
    total_memory = 0
    server_count = len(servers)

    for metrics in servers.values():
        total_cpu += metrics[0]
        total_memory += metrics[1]

    print(f"Number of Servers Monitored: {server_count}")
    print(f"Total CPU Usage: {total_cpu}, Average CPU Usage: {total_cpu / server_count:.2f}%")
    print(f"Total Memory Usage: {total_memory}, Average Memory Usage: {total_memory / server_count:.2f}%")




# Execute Functions
print("Analyzing Server Metrics:\n")
for server, metrics in server_metrics.items():
    analyze_server(server, metrics)

print("\nChecking Over-Utilized Servers:\n")
overutilized_servers = check_overutilized(server_metrics)
print("Over-Utilized Servers:", overutilized_servers)

print("\nGenerating Report:\n")
generate_report(server_metrics)


