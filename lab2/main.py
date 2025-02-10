import logging
logging.basicConfig(level="INFO")
class InvalidServerError(Exception):
    pass

valid_server = {
    "nginx", "docker", "apache", "tomcat", "mysql", "mariadb", "postgresql", "mongodb", "redis", "memcached",
    "rabbitmq", "kafka", "zookeeper", "elasticsearch", "logstash", "kibana", "prometheus", "grafana", "jenkins",
    "gitlab", "nexus", "sonarqube", "harbor", "minio", "portainer", "traefik", "consul", "vault", "nomad", "packer",
    "terraform", "ansible", "vagrant", "docker-compose", "kubernetes", "helm", "istio", "prometheus-operator",
    "grafana-operator", "kiali", "jaeger", "loki", "fluentd", "nginx-ingress", "cert-manager", "external-dns",
    "argocd", "tekton", "jenkins-x", "spinnaker", "argo-rollouts", "argo-cd", "argo-events", "argo-workflows",
    "argo-tunnel", "argo-registry", "argo-mlflow", "argo-cd-operator", "argo-rollouts-operator", "argo-events-operator",
    "argo-workflows-operator", "argo-tunnel-operator", "argo-registry-operator", "argo-mlflow-operator",
    "argo-cd-applicationset", "argo-rollouts-applicationset", "argo-events-applicationset", "argo-workflows-applicationset",
    "argo-tunnel-applicationset", "argo-registry-applicationset", "argo-mlflow-applicationset",
    "argo-cd-applicationset-operator", "argo-rollouts-applicationset-operator", "argo-events-applicationset-operator",
    "argo-workflows-applicationset-operator", "argo-tunnel-applicationset-operator", "argo-registry-applicationset-operator",
    "argo-mlflow-applicationset-operator"
}


def check_service_status(server_name):
    try:
        if server_name == "":
            raise InvalidServerError("Server name is empty.")
        if not server_name.isalnum():
            raise InvalidServerError("Server name must be alphanumeric.")
        if server_name not in valid_server:
            raise InvalidServerError("Server is not recognized.")
        else:
            return "Runing"
    except InvalidServerError:
        raise ValueError

while True:
        server_name = input("Enter a server name: ")
        server_name.strip()
        try:
            status = check_service_status(server_name)
            logging.info("User type valid server name.")
        except ValueError as err:
            logging.error("User type invalid server name.")
