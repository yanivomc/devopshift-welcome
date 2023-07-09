#!/bin/bash

NAMESPACE="default"      # Replace with the namespace of your Kubernetes Dashboard installation
SERVICE_ACCOUNT_NAME="admin-user"       # Replace with your desired service account name
CLUSTER_ROLE_NAME="cluster-admin"  # Replace with your desired custom ClusterRole name


# Create service account
kubectl create serviceaccount $SERVICE_ACCOUNT_NAME -n $NAMESPACE



TOKEN=$(kubectl create token $SERVICE_ACCOUNT_NAME -n $NAMESPACE -o jsonpath='{.status.token}')

echo "Admin Token: $TOKEN"
