#!/bin/bash

#Docker
sudo apt update
sudo apt install -y curl jq

# Install Docker
curl https://get.docker.com | sudo bash
sudo usermod -aG docker jenkins

# Docker login
docker login --username $DOCKER_USERNAME --password $DOCKER_PASSWORD

# Install Docker Compose
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install Ansible
sudo apt update 
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y

type ansible
type ansible-playbook

