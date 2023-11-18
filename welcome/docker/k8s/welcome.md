
### K8S PLAYGROUND
Welcome to K8S playground.
In this lab, you have access to KUBECTL and to VisualCode in a browser (IDE)
VSCODE IDE PASSWORD: devopshift


Once your terminal is available,
Allow a few moments for your k8s environments to bootstrap.

**To validate k8s is indeed running please run:**

    kubectl get all --n all-namespaces

## Please note reagarding your LB IP
You may create a service Type LOADBALANCER and user your external IP (shown on top of this page) and the exposed port for ex. IP:80


### Creating a simple test
Once all services are up,
**Option 1:** Run the following command in your Terminal:

    kubectl run nginx --image nginx
    kubectl get pods

---
Make sure the nginx pod is in runnig state and delete it by running

    kubectl delete pod nginx
