$sshKey="a3:b3:18:83:a7:24:ec:22:31:05:a2:37:15:ce:a0:b6"
doctl compute droplet create lb-1 --size s-2vcpu-4gb --wait --region sgp1 --image docker-20-04 --ssh-keys $sshKey --user-data "docker run -d -p 9001:9001 free17/ws-server"
$ip=doctl compute droplet list --format PublicIPv4 --no-header
echo $ip
#scp ./ws-server root@${ip}:ws-server
# scp ../../ws-server/target/debug/ws-server root@${ip}:ws-server
# ssh root@${ip} docker pull free17/ws-server
# ssh root@${ip} docker run -d -p 9001:9001 free17/ws-server
# docker pull free17/ws-server && docker run -d -p 9001:9001 free17/ws-server
#doctl compute droplet delete lb-1 -f