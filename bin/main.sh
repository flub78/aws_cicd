#!/bin/sh
echo "Create a CI/CD pipeline";

ansible $aws_jenkins -a "hostname"
ansible $aws_jenkins -a "uptime"

echo "bye";