

Simple PromQL Queries:

1. Total number of requests:
```
sum(app_requests_total)
```

2. Current number of active requests:
```
app_requests_inprogress
```

3. Average CPU usage over the last 5 minutes:
```
avg_over_time(app_cpu_usage_percent[5m])
```

4. Total number of errors in the last hour:
```
sum(increase(app_errors_total[1h]))
```

5. Current memory usage in GB:
```
app_memory_usage_bytes / 1e9
```

Advanced PromQL Queries:

6. Request rate per second over the last 5 minutes, grouped by endpoint:
```
sum(rate(app_requests_total[5m])) by (endpoint)
```

7. 95th percentile of request latency over the last 10 minutes:
```
histogram_quantile(0.95, sum(rate(app_request_latency_seconds_bucket[10m])) by (le, endpoint))
```

8. Error rate as a percentage of total requests in the last hour:
```
(sum(increase(app_errors_total[1h])) / sum(increase(app_requests_total[1h]))) * 100
```

9. Top 3 endpoints by request count in the last day:
```
topk(3, sum(increase(app_requests_total[24h])) by (endpoint))
```

10. Ratio of cache hits to total cache attempts over the last hour:
```
sum(increase(app_cache_hits_total[1h])) / (sum(increase(app_cache_hits_total[1h])) + sum(increase(app_cache_misses_total[1h])))
```

11. Average queue processing time for each queue over the last 30 minutes:
```
avg_over_time(app_queue_processing_time_seconds_sum[30m]) / avg_over_time(app_queue_processing_time_seconds_count[30m])
```

12. Correlation between CPU usage and active requests (over last hour):
```
corr_over_time(app_cpu_usage_percent[1h], app_requests_inprogress[1h])
```

These queries provide a range of insights:

- Basic metrics like total requests and current active requests
- Performance metrics like CPU and memory usage
- Error rates and types
- Request latencies, including percentiles
- Cache performance
- Queue processing times
- Correlations between different metrics

You can use these as a starting point and modify them based on your specific monitoring needs. Remember to adjust the time ranges (`[5m]`, `[1h]`, etc.) as needed for your use case.