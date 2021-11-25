#!/bin/sh
echo "Create a CI/CD pipeline";

ansible aws_jenkins -a "hostname"
ansible aws_jenkins -a "uptime"

ansible-playbook ansible/aws_dev_server.yml

echo "bye";