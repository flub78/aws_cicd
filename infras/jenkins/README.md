# This is a terraform project to deploy a Jenkins server

## Usage

everything is described in the install.sh script.

If you need to change the server name or domain edit the terraform.tfvars ans install.sh files.

## SSH to the jenkins machine

    ec2 -n tf-jenkins -r
    
    ssh -i $TF_VAR_PRIVATE_KEY ubuntu@jenkins.flub78.net

    http://jenkins.flub78.net:8080/