#!/bin/bash
echo "### Installing HELM"
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
echo "##############################"
echo "### installing K8S Dashboard"
curl -fsSL -o Values.yaml https://raw.githubusercontent.com/yanivomc/devopshift-welcome/master/welcome/k8s/dashboard/Values.yaml
helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dmespace --namespace kubernetes-dashboard -f Values.yaml


echo "##############################"
echo "### Configure USER account"
NAMESPACE="default"      # Replace with the namespace of your Kubernetes Dashboard installation
SERVICE_ACCOUNT_NAME="admin-user"       # Replace with your desired service account name
CLUSTER_ROLE_NAME="cluster-admin"  # Replace with your desired custom ClusterRole name


# Create service account
kubectl create serviceaccount $SERVICE_ACCOUNT_NAME -n $NAMESPACE



TOKEN=$(kubectl create token $SERVICE_ACCOUNT_NAME -n $NAMESPACE -o jsonpath='{.status.token}')

echo "Admin Token:"
echo
echo  "$TOKEN"
