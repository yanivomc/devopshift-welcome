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



