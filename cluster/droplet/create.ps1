$ip=doctl compute droplet create temp-deoplet --count 2 --size s-4vcpu-8gb --update-kubeconfig --wait --region sgp1
scp ../../ws-server/target/debug/ws-server root@${ip}:ws-server
ssh root@${ip} ./ws-server