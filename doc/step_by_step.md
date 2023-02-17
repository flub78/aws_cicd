# Step by step CI/CD Pipeline creation.

This is an example of creation and population of an EC2 instance.

## Pre-conditions and pre-requisites

Even if the goal is to become 100 % automated and scripted, the first version of this script will is based on the following assumption.

- the AMI is hardcoded in the script

### Environment variables

The environment variables to control the CI/CD creation are defined in the setenv.sh file.

Secrets and credential must be stored outside of the github project or kept encrypted in the Ansible vault.

## Key generation

First a RSA key needs to be generated, this key will be used to create an AWS key pair and for ssh and ansible connection

```
ssh-keygen -t rsa -f $TF_VAR_PRIVATE_KEY
```

## Infrastructure provisioning

```
cd infras/jenkins
terraform apply
```

By default this terraform configuration creates an EC2 instance that can be accessed from ssh. 

## SSH connection

Once the instance is up and running it is possible to login using the default user and DNS address. The domain name can be used if you wait long enough for the DNS tables to be propagated.

```
ssh -i $TF_VAR_PRIVATE_KEY ubuntu@ec2-52-47-144-86.eu-west-3.compute.amazonaws.com

or

ssh -i $TF_VAR_PRIVATE_KEY ubuntu@web.flub78.net
```


https://linuxbeast.com/tutorials/aws/ssh-without-password-on-linux-amazon-ec2-ubuntu/


## Creation of an alarm for automatic shutdown

As EC2 instances can be pretty expensive it is useful to have them automatically stopping when they are not used.
Currently it can be done from the AWS console, by clicking on the cross close to "Alarm status"


## Populating with Ansible

### Declaring the host

A basic hosts file cat be derived from the terraform outputs.


    vi hosts
    [jenkins]
        ubuntu@web.flub78.net


### Test

A simple command

```java
ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/test_connection.yml

PLAY [Network Getting Started First Playbook] ***********************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [ubuntu@web.flub78.net]

TASK [test connection] **********************************************************************************************************************************************************************
ok: [ubuntu@web.flub78.net]

TASK [test root access] *********************************************************************************************************************************************************************
changed: [ubuntu@web.flub78.net]

PLAY RECAP **********************************************************************************************************************************************************************************
ubuntu@web.flub78.net      : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Then you can run the ansible roles

```java
ansible-playbook --inventory hosts --key-file $TF_VAR_PRIVATE_KEY $PLAYBOOK/lamp.yml
```