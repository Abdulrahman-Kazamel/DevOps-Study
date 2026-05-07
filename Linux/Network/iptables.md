

```bash
cat user-data.sh
#!/bin/bash

yes | sudo yum update
yes | sudo yum install iptables-services

sudo systemctl start iptables
sudo systemctl enable iptables

sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

sudo service iptables save
```


## it worked only this way
```bash
#After many tries, the configuration script which worked perfectly for me on the #Amazon Linux 2023 (AMI like "_al2023-ami-2023_*") NAT instance was:


sudo yum install iptables-services -y
sudo systemctl enable iptables
sudo systemctl start iptables

# Turning on IP Forwarding
sudo touch /etc/sysctl.d/custom-ip-forwarding.conf
sudo chmod 666 /etc/sysctl.d/custom-ip-forwarding.conf
sudo echo "net.ipv4.ip_forward=1" >> /etc/sysctl.d/custom-ip-forwarding.conf
sudo sysctl -p /etc/sysctl.d/custom-ip-forwarding.conf

# Making a catchall rule for routing and masking the private IP
sudo /sbin/iptables -t nat -A POSTROUTING -o ens5 -j MASQUERADE
sudo /sbin/iptables -F FORWARD
sudo service iptables save
```



```