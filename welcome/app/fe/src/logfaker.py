import json
import random
import time
from datetime import datetime, timedelta
from faker import Faker
import socket

fake = Faker()

def hostname():
    # Get real machine/container hostname from os and return it 
    hostname = socket.gethostname()
    return hostname



def generate_log_entry():
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
    app_names = ["user-service", "product-service", "order-service", "auth-service", "search-service"]
    http_methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
    endpoints = ["/api/users", "/api/products", "/api/orders", "/api/auth", "/api/search"]
    
    timestamp = fake.date_time_between(start_date="-1h", end_date="now").isoformat()
    level = random.choice(log_levels)
    

    
    log_entry = {
        "timestamp": timestamp,
        "level": level,
        "service": fake.word(ext_word_list=["user-service", "product-service", "order-service", "auth-service", "search-service"]),
        "trace_id": fake.uuid4(),
        "span_id": fake.uuid4(),
        "commit": fake.sha1(),
        "user_id": fake.uuid4(),
        "ip_address": fake.ipv4(),
        "user_agent": fake.user_agent(),
        "method": random.choice(http_methods),
        "endpoint": random.choice(endpoints),
        "status_code": fake.random_element(elements=(200, 201, 204, 400, 401, 403, 404, 500)),
        "response_time": round(random.uniform(0.1, 2.0), 3),
        "message": fake.sentence(),
        "hostname": hostname(),
        "app_name": random.choice(app_names),
    }
    
    if level == "ERROR":
        log_entry["error_type"] = fake.word(ext_word_list=["ValidationError", "DatabaseError", "NetworkError", "AuthenticationError"])
        log_entry["stack_trace"] = fake.text()
    
    if log_entry["method"] in ["POST", "PUT", "PATCH"]:
        log_entry["request_body_size"] = fake.random_int(min=10, max=10000)
    
    if log_entry["endpoint"] == "/api/search":
        log_entry["search_query"] = fake.word()
        log_entry["results_count"] = fake.random_int(min=0, max=100)
    
    return log_entry

def main():
    while True:
        log_entry = generate_log_entry()
        print(json.dumps(log_entry))
        time.sleep(random.uniform(0.1, 1))

# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\nLog generation stopped.")