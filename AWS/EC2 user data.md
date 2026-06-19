
```bash
#!/bin/bash
# Update the local package index to ensure the latest versions are available
yes|sudo apt update -y

# Install Nginx automatically without manual confirmation
#apt install nginx -y
yes| sudo apt install apache2 -y
# Ensure Nginx starts immediately and restarts automatically on boot
sudo systemctl start apache2
sudo systemctl enable apache2

```


```

#!/bin/bash
# Update the local package index to ensure the latest versions are available
yes |  apt update 
yes | apt install apache2 



# and this installation will start it automatically

```



### troubleshooting

```bash
tail -3000 /var/log/cloud-init-output.log

```



### docker and nginx installation, multi layer temp source


```bash
#!/bin/bash

#update system

sudo apt iinstall update

##install nginx

yes |  sudo apt install nginx


##install docker 

sudo apt remove $(dpkg --get-selections docker.io docker-compose docker-compose-v2 docker-doc podman-docker containerd runc | cut -f1)


# Add Docker's official GPG key:
sudo apt update
yes |  sudo apt install ca-certificates curl 
yes |  sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update


yes |  sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


sudo systemctl start docker



```


```bash
#!/bin/bash 
yes | dnf install httpd 
systemctl enable httpd 
systemctl start httpd 
yes | dnf install wget unzip 
cd /tmp 
wget -O luminary.zip https://templatemo.com/tm-zip-files-2020/templatemo_621_luminary.zip

mkdir luminary
unzip luminary.zip  -d luminary/
mv luminary/* /var/www/html/
##this should be added like this because each template come with its names 
mv  /var/www/html/templatemo_621_luminary/* /var/www/html/

systemctl restart httpd
```


