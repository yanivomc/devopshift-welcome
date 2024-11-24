First we are going to install helm:


curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh

Next we are going to install metricserver and kubestate metrics

kubectl apply -f ./kubestatemetrics/.


Next Install Node Exporter
Node exporter is a Prometheus exporter for hardware and OS metrics exposed by *nix kernels.

Using Helm:
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus-node-exporter prometheus-community/prometheus-node-exporter


Recommended Dashboards
Kubernetes / Views / Global

Provides an overview of the entire Kubernetes cluster, including CPU and memory usage, disk usage, and more.
GitHub Link: Kubernetes Views Global
Kubernetes / Nodes

Focuses on node-level metrics such as CPU, memory, and disk usage.
GitHub Link: Kubernetes Views Nodes
Kubernetes / Pods

Displays metrics at the pod level, including CPU and memory usage.
GitHub Link: Kubernetes Views Pods
Kubernetes / Namespaces

Provides metrics organized by namespaces, useful for multi-tenant environments.
GitHub Link: Kubernetes Views Namespaces
