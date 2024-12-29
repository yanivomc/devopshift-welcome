def restart_service(service_name):
    return f"Restarting {service_name}..."

def check_service_status(service_name):
    return "Running" if service_name in ["nginx", "docker"] else "Stopped"