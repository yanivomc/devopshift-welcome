Into our Promtheus config map we need to append the following scraper job: 
 
 ```bash
 scrape_configs:
      - job_name: 'fefaker'
        kubernetes_sd_configs:
          - role: service
            namespaces:
              names:
                - default  # adjust if your app is in a different namespace
        relabel_configs:
          - source_labels: [__meta_kubernetes_service_name]
            regex: fe-service
            action: keep
          - source_labels: [__meta_kubernetes_service_port_name]
            regex: .*metrics.*
            action: keep
          - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape]
            regex: "true"
            action: keep
        metrics_path: /metrics
        scheme: http
```


Once updated please run: 
kubectl rollout restart deployment prometheus -n [Prometheus Namespace]