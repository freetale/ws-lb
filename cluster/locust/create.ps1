doctl kubernetes cluster create temp-locust --count 5 --size c-4 --update-kubeconfig --wait --region sgp1
kubectl apply -k ./kustomization/
#doctl kubernetes cluster delete temp-locust