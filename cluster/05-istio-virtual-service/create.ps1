doctl kubernetes cluster create lb-ingress --count 1 --size s-4vcpu-8gb  --update-kubeconfig --wait --region sgp1
istioctl install -y
kubectl label namespace default istio-injection=enabled

kubectl apply -k ./kustomization/
kubectl get svc -w -A
#doctl kubernetes cluster delete lb-ingress