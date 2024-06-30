#!/bin/bash

ROOTFOLDER="/home/ubuntu/workarea/devopshift/welcome/istio/"

# Function to prompt user for installation choice
function prompt_installation_choice() {
    echo "Choose installation option:"
    echo "1. Install all components (Istio, Kiali, Prometheus, Jaeger)"
    echo "2. Install only Istio"
    read -rp "Enter your choice (1 or 2): " choice
    return $choice
}

# Function to run a command with retries
function run_command() {
    command=$1
    description=$2
    retries=3
    sleep_duration=10

    for ((i=1; i<=retries; i++)); do
        echo "Running: $description (Attempt $i of $retries)"
        if $command; then
            return 0
        fi
        echo "Retry $i of $retries failed. Retrying in $sleep_duration seconds..."
        sleep $sleep_duration
    done

    echo "Error: $description failed after $retries attempts."
    exit 1
}

# Function to install Istio
function install_istio() {
    echo "Installing Istio..."
    run_command "sudo cp ${ROOTFOLDER}/istio-1.22.1/bin/istioctl /usr/sbin/" "Copy istioctl to /usr/sbin"
    run_command "istioctl operator init" "Initialize the Istio Operator"
    run_command "kubectl get pods -n istio-operator" "Verify the Istio Operator installation"
    run_command "kubectl apply -f ${ROOTFOLDER}/istio-1.22.1/istio-manifest.yaml" "Apply the Istio custom resource"
    run_command "istioctl verify-install" "Verify the Istio installation"
    run_command "kubectl get pods -n istio-system" "Check Istio system pods"
}

# Function to install Kiali
function install_kiali() {
    echo "Installing Kiali..."
    run_command "kubectl apply -f ${ROOTFOLDER}/kiali/kiali-deployment.yaml" "Apply the Kiali deployment manifest"
    run_command "kubectl get pods -n istio-system" "Verify the Kiali deployment"
}

# Function to install Prometheus
function install_prometheus() {
    echo "Installing Prometheus..."
    run_command "kubectl apply -f ${ROOTFOLDER}/prometheus/prometheus-deployments.yaml" "Apply the Prometheus deployment manifest"
    run_command "kubectl get pods -n istio-system" "Verify the Prometheus deployment"
}

# Function to install Jaeger
function install_jaeger() {
    echo "Installing Jaeger..."
    run_command "kubectl apply -f ${ROOTFOLDER}/jaeger/jaeger-deployment.yaml" "Apply the Jaeger deployment manifest"
    run_command "kubectl get pods -n istio-system" "Verify the Jaeger deployment"
}

# Function to expose services using VirtualServices
function expose_services() {
    echo "Exposing services..."
    run_command "kubectl apply -f ${ROOTFOLDER}/kiali/kiali-GatwewayAndVirtualservice.yaml" "Apply Gateway and VirtualService configurations"
    run_command "kubectl get gateways -n istio-system" "Check the Gateway"
    run_command "kubectl get virtualservices -n istio-system" "Check the VirtualService"
    run_command "kubectl get endpoints -n istio-system" "Check the endpoints"
}

# Function to validate installation and output endpoints
function validate_installation() {
    echo "Validating Istio installation..."
    istioctl verify-install

    ingress_ip=$(kubectl get svc istio-ingressgateway -n istio-system -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
    # if ingress_ip is empty retry check after 5 seconds for 3 times and update the user on the process status
    if [ -z "$ingress_ip" ]; then
    for i in {1..3}; do
        echo "Waiting for Istio Ingress Gateway IP... retry $i/3"
        sleep 5
        ingress_ip=$(kubectl get svc istio-ingressgateway -n istio-system -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
        if [ ! -z "$ingress_ip" ]; then
        break
        fi
    done
    #   if Loop ends and ingress_ip is still empty, then update the user on the process status
    if [ -z "$ingress_ip" ]; then
        echo "Istio Ingress Gateway IP not found yet - please run the command again manually to get the IP."
        echo "kubectl get svc istio-ingressgateway -n istio-system -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'"
        else
        echo "Istio Ingress Gateway IP: $ingress_ip"
    fi
    fi


    echo "Access the following URLs to check the services:"
    echo "Kiali: http://$ingress_ip/kiali"
    echo "Jaeger: http://$ingress_ip/jaeger"
    echo "Prometheus: http://$ingress_ip/prometheus"
}

# Main script execution
prompt_installation_choice
choice=$?

if [ "$choice" -eq 1 ]; then
    install_istio
    install_kiali
    install_prometheus
    install_jaeger
    expose_services
    validate_installation
elif [ "$choice" -eq 2 ]; then
    install_istio
    validate_installation
else
    echo "Invalid choice. Exiting."
    exit 1
fi
