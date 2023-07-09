#!/bin/bash
echo "### Installing HELM"
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
echo "##############################"
echo "### installing K8S Dashboard"
curl -fsSL -o Values.yaml https://raw.githubusercontent.com/yanivomc/devopshift-welcome/master/welcome/k8s/dashboard/Values.yaml
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dmespace --namespace kubernetes-dashboard -f Values.yaml


echo "##############################"
echo "### Configure USER roles"
curl -fsSL -o generate-user-token.yaml https://raw.githubusercontent.com/yanivomc/devopshift-welcome/master/welcome/k8s/dashboard/generate-user-token.yaml
kubectl apply -f generate-user-token.yaml
echo "##############################"
echo "### Configure USER account"
NAMESPACE="kubernetes-dashboard"      # Replace with the namespace of your Kubernetes Dashboard installation
SERVICE_ACCOUNT_NAME="admin-user"      # Replace with your desired service account name

# Delete existing service account
kubectl delete serviceaccount $SERVICE_ACCOUNT_NAME -n $NAMESPACE --ignore-not-found=true

# Create namespace
kubectl create namespace $NAMESPACE

# Create service account
kubectl create serviceaccount $SERVICE_ACCOUNT_NAME -n $NAMESPACE

# Bind the cluster-admin ClusterRole to the service account
kubectl create clusterrolebinding $SERVICE_ACCOUNT_NAME-cluster-admin-binding --clusterrole=cluster-admin --serviceaccount=$NAMESPACE:$SERVICE_ACCOUNT_NAME

# Get the token associated with the service account
SECRET_NAME=$(kubectl get serviceaccount $SERVICE_ACCOUNT_NAME -n $NAMESPACE -o jsonpath='{.secrets[0].name}')


TOKEN=$(kubectl create token $SERVICE_ACCOUNT_NAME -n $NAMESPACE -o jsonpath='{.status.token}')

echo "Admin Token:"
echo
echo  "$TOKEN"
