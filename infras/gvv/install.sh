#!/usr/bin/bash

# Infrastructure configuration
cd ~/aws_cicd/infras/gvv
terraform init
terraform apply -auto-approve
source ansible.setenv

# Delete previous ssh key
ssh-keygen -f "/home/frederic/.ssh/known_hosts" -R "gvv.flub78.net"

# Ansible roles 
ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/lamp.yml
ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/gvv.yml

# For debugging
# ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/lamp.yml --tags "debug" --start-at-task="phpmyadmin : Display php version"	




