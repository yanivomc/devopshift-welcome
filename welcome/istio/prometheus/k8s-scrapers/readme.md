First we are going to install helm:


curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh


Next we are going to install metricserver and kubestate metrics

kubectl apply -f ./kubestatemetrics/.
