doctl kubernetes cluster create temp-locust --count 9 --size c-4 --update-kubeconfig --wait --region sgp1
kubectl apply -k ./kustomization/
kubectl get svc -w
#doctl kubernetes cluster delete temp-locust -f