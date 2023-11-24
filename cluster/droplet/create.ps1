$ip=doctl compute droplet create temp-deoplet --size s-2vcpu-4gb --wait --region sgp1 --image docker-20-04
scp ../../ws-server/target/debug/ws-server root@${ip}:ws-server
ssh root@${ip} ./ws-server