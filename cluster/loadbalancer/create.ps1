doctl kubernetes cluster create lb-ingress --count 1 --size s-2vcpu-4gb  --update-kubeconfig --wait --region sgp1
kubectl apply -k ./kustomization/
kubectl get svc -w
#doctl kubernetes cluster delete lb-ingress