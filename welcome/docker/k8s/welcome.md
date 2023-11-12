
### K8S PLAYGROUND
Welcome to K8S playground.

Once your terminal is available,
Allow a few moments for your k8s environments to bootstrap.

**To validate k8s is indeed running please run:**

    kubectl get all --n all-namespaces


### Creating a simple test
Once all services are up,


**Option 1:** Run the following command in your Terminal:

    kubectl run nginx --image nginx
    kubectl get pods

---
Make sure the nginx pod is in runnig state and delete it by running

    kubectl delete pod nginx