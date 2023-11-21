doctl kubernetes cluster create temp-load --count 2 --size s-4vcpu-8gb --update-kubeconfig --wait
kubectl apply -k ./kustomization/
#doctl kubernetes cluster delete temp-load