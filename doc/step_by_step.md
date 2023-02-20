# Step by step CI/CD Pipeline creation.

This is an example of creation and population of an EC2 instance.

## Pre-conditions and pre-requisites

### Environment variables

The environment variables to control the CI/CD creation are defined in the setenv.sh file.

Secrets and credential are stored outside of the github project or kept encrypted in the Ansible vault.

## Key generation

Generate a RSA key that will be imported in a AWS key pair and for ssh and ansible connection.

```
ssh-keygen -t rsa -f $TF_VAR_PRIVATE_KEY
```

## Infrastructure provisioning

```
cd infras/jenkins
terraform init
terraform plan
terraform apply
```

By default this terraform configuration creates an EC2 instance that can be accessed from ssh. 

## SSH connection

Once the instance is up and running it is possible to login using the default user and DNS address. To use the domain name wait for the DNS tables to be propagated.

```
ssh -i $TF_VAR_PRIVATE_KEY ubuntu@ec2-52-47-144-86.eu-west-3.compute.amazonaws.com

or

ssh -i $TF_VAR_PRIVATE_KEY ubuntu@ratus.flub78.net
```

### Documentation reference
https://linuxbeast.com/tutorials/aws/ssh-without-password-on-linux-amazon-ec2-ubuntu/


## Populating with Ansible

### Ansible input files

Terraform generates an ansible inventory named hosts and an ansible.setenv file to pass information from
terraform to ansible.

    cat hosts
    source ansible.setenv


### Test

A simple command

```java
ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/test_connection.yml

PLAY [Network Getting Started First Playbook] ***********************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [ubuntu@ratus.flub78.net]

TASK [test connection] **********************************************************************************************************************************************************************
ok: [ubuntu@ratus.flub78.net]

TASK [test root access] *********************************************************************************************************************************************************************
changed: [ubuntu@ratus.flub78.net]

PLAY RECAP **********************************************************************************************************************************************************************************
ubuntu@ratus.flub78.net      : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Others playbooks

```java
source ansible.setenv
ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/lamp.yml
```