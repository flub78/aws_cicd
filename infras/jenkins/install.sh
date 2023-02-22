#!/usr/bin/bash

# Install Jenkins
terraform init
terraform apply -auto-approve
source ansible.setenv

# ssh-keygen -f "/home/frederic/.ssh/known_hosts" -R "ratus.flub78.net"

ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/lamp.yml
# ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/jenkins.yml