#!/usr/bin/bash

# Infrastructure configuration
cd ~/aws_cicd/infras/jenkins
terraform init
terraform apply -auto-approve
source ansible.setenv

# Delete previous ssh key
ssh-keygen -f "/home/frederic/.ssh/known_hosts" -R "jenkins.flub78.net"

# Ansible roles, lamp, jenkins
ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/test_connection.yml

ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/lamp.yml

ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/jenkins.yml

ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/jenkins_jobs_multi.yml

# Jenkins configuration

Until now there is still a manual step in the jenkins configuration. Once jenkins is installed the user must go to the web interface and provide tha password to unlock jenkins.

TODO: automate the initial jenkins connection and first user creation
TODO: automate the creation of token for jenkins-cli


# Install jenkins modules
cd ~/jenkins-cli
java -jar jenkins-cli.jar -s http://jenkins.flub78.net:8080/ -auth @jenkins_token who-am-i

# jenkins shortcut
# export JENKINS_USER_ID=jenkins
# export JENKINS_API_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxx
# export JENKINS_URL=http://jenkins.flub78.net:8080

alias jenkins='java -jar jenkins-cli.jar -s http://jenkins.flub78.net:8080/ -auth @jenkins_token'
jenkins install-plugin phing
jenkins install-plugin htmlpublisher
jenkins install-plugin plot
jenkins install-plugin jdepend
jenkins install-plugin subversion
jenkins install-plugin violations
jenkins install-plugin warnings-ng
jenkins safe-restart

ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/jenkins_jobs_multi.yml


