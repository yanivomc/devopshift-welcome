from prometheus_client import start_http_server, Gauge, Counter, Histogram, Summary
import random
import time
import logfaker as logerfaker

# Request metrics
REQUEST_INPROGRESS = Gauge('app_requests_inprogress', 'Number of application requests in progress')
REQUEST_COUNTER = Counter('app_requests_total', 'Total number of application requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency in seconds', ['endpoint'])

# Error metrics
ERROR_COUNTER = Counter('app_errors_total', 'Total number of application errors', ['type'])

# System metrics
CPU_USAGE = Gauge('app_cpu_usage_percent', 'Current CPU usage in percent')
MEMORY_USAGE = Gauge('app_memory_usage_bytes', 'Current memory usage in bytes')
DISK_USAGE = Gauge('app_disk_usage_percent', 'Current disk usage in percent')

# Database metrics
DB_CONNECTIONS = Gauge('app_db_connections', 'Number of current database connections')
DB_QUERIES = Counter('app_db_queries_total', 'Total number of database queries', ['type'])
DB_QUERY_LATENCY = Histogram('app_db_query_latency_seconds', 'Database query latency in seconds')

# Cache metrics
CACHE_HITS = Counter('app_cache_hits_total', 'Total number of cache hits')
CACHE_MISSES = Counter('app_cache_misses_total', 'Total number of cache misses')

# Message queue metrics
QUEUE_SIZE = Gauge('app_queue_size', 'Current number of items in the queue', ['queue'])
QUEUE_PROCESSING_TIME = Histogram('app_queue_processing_time_seconds', 'Time taken to process a queue item', ['queue'])

# Custom business metrics
ACTIVE_USERS = Gauge('app_active_users', 'Number of active users')
SALES_TOTAL = Counter('app_sales_total_dollars', 'Total sales in dollars')

# Endpoints and services
ENDPOINTS = ['/api/users', '/api/orders', '/api/products', '/api/payments']
SERVICES = ['user_service', 'order_service', 'product_service', 'payment_service']

# Create service health metrics
SERVICE_HEALTH = {service: Gauge(f'{service}_health', f'Health of {service} (0=unhealthy, 1=healthy)') for service in SERVICES}

def generate_fake_metrics():
    while True:
        # Request metrics
        REQUEST_INPROGRESS.set(random.randint(0, 100))
        for method in ['GET', 'POST', 'PUT', 'DELETE']:
            for endpoint in ENDPOINTS:
                for status in ['200', '404', '500']:
                    REQUEST_COUNTER.labels(method=method, endpoint=endpoint, status=status).inc(random.randint(0, 10))
                REQUEST_LATENCY.labels(endpoint=endpoint).observe(random.uniform(0.001, 10.0))

        # Error metrics
        for error_type in ['connection_error', 'validation_error', 'internal_error']:
            ERROR_COUNTER.labels(type=error_type).inc(random.randint(0, 5))

        # System metrics
        CPU_USAGE.set(random.uniform(0, 100))
        MEMORY_USAGE.set(random.randint(100_000_000, 1_000_000_000))
        DISK_USAGE.set(random.uniform(0, 100))

        # Database metrics
        DB_CONNECTIONS.set(random.randint(1, 100))
        for query_type in ['select', 'insert', 'update', 'delete']:
            DB_QUERIES.labels(type=query_type).inc(random.randint(0, 50))
        DB_QUERY_LATENCY.observe(random.uniform(0.001, 1.0))

        # Cache metrics
        CACHE_HITS.inc(random.randint(0, 100))
        CACHE_MISSES.inc(random.randint(0, 20))

        # Message queue metrics
        for queue in ['email', 'logging', 'export']:
            QUEUE_SIZE.labels(queue=queue).set(random.randint(0, 1000))
            QUEUE_PROCESSING_TIME.labels(queue=queue).observe(random.uniform(0.1, 60))

        # Custom business metrics
        ACTIVE_USERS.set(random.randint(100, 10000))
        SALES_TOTAL.inc(random.uniform(0, 1000))

        # Service health
        for service in SERVICES:
            SERVICE_HEALTH[service].set(random.choice([0, 1]))

        # Wait before generating next batch of metrics
        time.sleep(5)

# Create a new thread that will run the logerfaker.main() function  
# in parallel to the generate_fake_metrics() function
import threading
def loger():
    
    log_thread = threading.Thread(target=logerfaker.main)
    log_thread.start()


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    print("Metrics server started on port 8000")
    print("Press Ctrl+C to stop metrics generation.")
    try:
        
        loger()
        generate_fake_metrics()
        
    except KeyboardInterrupt:
        print("\nMetrics generation stopped.")
        print("\nLog generation stopped.")
