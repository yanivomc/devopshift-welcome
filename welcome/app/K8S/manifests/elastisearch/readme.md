# Quick Guide on how to install ECK (Elastic Cloud Operator)

This guide provides a quick overview of how to deploy and use ECK


- [Installation of operator](#installation)
- [Deploy cluster](#deploy-cluster)

## Installation
If installed on an istio based cluster , please run the following first:

Create the name space manualy for the operator 
```bash
kubectl create namespace elastic-system
```
Enable istio sidecar auto inject on the namespace
```bash
kubectl label namespace elastic-system istio-injection=enabled
```
Validate:
```bash
kubectl get namespace -L istio-injection
```

Continue to the next step on completion of the above steps or when not installed on an ISTIO Based cluster:

Install the ECK Operator
```bash
kubectl apply -f https://download.elastic.co/downloads/eck/2.8.0/crds.yaml
kubectl apply -f https://download.elastic.co/downloads/eck/2.8.0/operator.yaml
```

Verify the Installation:
Hold a few moments - ignore crashloopback for a moment and it suppose to be resolved

```bash
kubectl get pods -n elastic-system
```

## deploy-cluster
Deploy Elasticsearch Cluster
```bash
cd /home/ubuntu/workarea/devopshift/welcome/app/K8S/manifests/elastisearch
kubectl apply -f elasticsearch.yaml
```
Validate: Wait a minute or until the pods are in state running
```bash
kubectl get Elasticsearch
NAME         HEALTH   NODES   VERSION   PHASE   AGE
quickstart   green    1       8.2.0     Ready   3m13s
```

# deploy-kibana
Deploy kibana manifest
```bash
kubectl apply -f kibana.yaml
```
Validate: Wait a minute or until the pods are in state running
```bash
kubectl get kibana
NAME         HEALTH   NODES   VERSION   AGE
quickstart   green    1       8.2.0     74s
```

## Access-Kibana
Get LB Endpoint for kibana
```bash
endpoint=$(kubectl get svc quickstart-kb-http  -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
echo "Your Kibana Endpoint is : http://$endpoint:5601"
```

There is no user/password enabled

## Deploy all the rest
Once kibana is working and elasticsearch is green 
```bash
kubectl apply -f .
```
this will install and verify that everything is set along with metricbeat and filebeat


## view logs 
In kibana go to :
observbility > logs

## View Metricbeat dashboard K8S
In Kibana go to:
Dashboard > [Metricbeat Kubernetes] Overview ECS

