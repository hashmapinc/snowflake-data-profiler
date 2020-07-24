#!bin/bash

# run this script with sudo

# installations
yum update -y
yum install -y docker git

# prepare docker
sudo usermod -aG docker ec2-user
sudo service docker start

# docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose