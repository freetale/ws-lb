doctl  kubernetes cluster create temp-ws --size s-4vcpu-8gb --count 1 --size c-4 --update-kubeconfig --wait --region sgp1
scp 
#doctl kubernetes cluster delete temp-ws