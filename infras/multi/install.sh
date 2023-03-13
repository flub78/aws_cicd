#!/usr/bin/bash

#
#

# Infrastructure configuration
cd ~/aws_cicd/infras/multi
terraform init
terraform apply -auto-approve
source ansible.setenv

# Delete previous ssh key
ssh-keygen -f "/home/frederic/.ssh/known_hosts" -R "multi.flub78.net"

# Ansible roles lamp
ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/lamp.yml




