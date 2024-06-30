# Quick Guide: Creating Prometheus Metrics in Python

This guide provides a quick overview of how to create and use Prometheus metrics in Python applications using the `prometheus_client` library.

## Table of Contents
- [Installation](#installation)
- [Metric Types](#metric-types)
  - [Counter](#1-counter)
  - [Gauge](#2-gauge)
  - [Histogram](#3-histogram)
  - [Summary](#4-summary)
- [Labels](#labels)
- [Exposing Metrics](#exposing-metrics)

## Installation

First, install the `prometheus_client` library:

```bash
pip install prometheus_client
```

## Metric Types

Prometheus offers four main types of metrics:

### 1. Counter

A Counter is a cumulative metric that represents a single monotonically increasing counter whose value can only increase or be reset to zero.

```python
from prometheus_client import Counter

REQUEST_COUNT = Counter('request_count_total', 'Total number of requests')

# Increment the counter
REQUEST_COUNT.inc()

# Increment by a specific amount
REQUEST_COUNT.inc(5)
```

Use for: Number of requests, tasks completed, errors occurred.

### 2. Gauge

A Gauge is a metric that represents a single numerical value that can arbitrarily go up and down.

```python
from prometheus_client import Gauge

ACTIVE_REQUESTS = Gauge('active_requests', 'Number of active requests')

# Set a value
ACTIVE_REQUESTS.set(15)

# Increment/decrement
ACTIVE_REQUESTS.inc()
ACTIVE_REQUESTS.dec(2)
```

Use for: Memory usage, CPU usage, concurrent requests.

### 3. Histogram

A Histogram samples observations and counts them in configurable buckets. It also provides a sum of all observed values.

```python
from prometheus_client import Histogram

REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency in seconds',
                            buckets=[0.1, 0.5, 1, 2, 5, 10])

# Observe a value
REQUEST_LATENCY.observe(0.7)
```

Use for: Request durations, response sizes.

### 4. Summary

Similar to a Histogram, a Summary samples observations. It provides a total count of observations and a sum of all observed values, and calculates configurable quantiles over a sliding time window.

```python
from prometheus_client import Summary

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Observe a value
REQUEST_TIME.observe(0.5)
```

Use for: Request durations, response sizes (when you need φ-quantiles).

## Labels

You can add labels to your metrics for more detailed monitoring:

```python
from prometheus_client import Counter

REQUEST_COUNT = Counter('request_count_total', 'Total number of requests', 
                        ['method', 'endpoint'])

REQUEST_COUNT.labels(method='GET', endpoint='/api/users').inc()
```

## Exposing Metrics

To expose the metrics:

```python
from prometheus_client import start_http_server

if __name__ == '__main__':
    start_http_server(8000)
    # Your application code here
```

This starts a server on port 8000, exposing your metrics at `http://localhost:8000`.

---

Remember, when choosing between Histogram and Summary:
- Use Histogram if you need to aggregate metrics from multiple instances or if you need to calculate percentiles for very long periods.
- Use Summary if you need accurate quantiles and don't need to aggregate metrics from multiple instances.
