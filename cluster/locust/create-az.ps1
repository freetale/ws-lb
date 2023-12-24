az aks create -g locust -n temp-locust --node-count 10 --generate-ssh-keys
az aks get-credentials --resource-group locust --name temp-locust
kubectl apply -k ./kustomization/
kubectl get svc -w
#doctl kubernetes cluster delete temp-locust -f