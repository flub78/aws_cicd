# Step by step CI/CD Pipeline creation.

This is an example of creation and population of an EC2 instance.

## Pre-conditions and pre-requisites

Even if the goal is to become 100 % automated and scripted, the first version of this script will is based on the following assumption.

- the AMI is hardcoded in the script
- there is an existing security group allowing ssh access and HTTP and HTTPS requests

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
cd terraform/cicf
terraform apply
```

The existing keys can be listed with

    ./key_pair.py -l

    frederic@LAPTOP-57QER3OP:~/aws_cicd/python$ ./key_pair.py -l
        JenkinsKeyPair key-0ab43bc7c2096e6f4 rsa
        jenkins_key_pair2 key-06bf11f5bdc28feeb rsa
        cicd key-0d57982c1856230ee rsa
        ratus_ec2-keypair key-0b76bf8ab760d67f6 rsa

    $ key_pair.py
    cicd key-0d57982c1856230ee rsa
    ratus_ec2-keypair key-0b76bf8ab760d67f6 rsa
    terraform-key key-09ee6b34c67b38d36 rsa

And later the key can be deleted with 

    ./key_pair.py -d -n mina_keypair

## SSH connection

Once the instance is up and running it is possible to login using the default user and DNS address.

    ssh -i $TF_VAR_PRIVATE_KEY ubuntu@ec2-52-47-144-86.eu-west-3.compute.amazonaws.com

    https://linuxbeast.com/tutorials/aws/ssh-without-password-on-linux-amazon-ec2-ubuntu/


## Creation of an alarm for automatic shutdown

As EC2 instances can be pretty expensive it is useful to have them automatically stopping when they are not used.
Currently it can be done from the AWS console, by clicking on the cross close to "Alarm status"

## Association of the instance with an elastic IP address

By default instances get dynamic IP addresses which cannot be targetted by S3 routes. It is important to identify the logical entry points of a system and associate them with a domain name. So once an instance has a role the related elastic IP address has to be associated with this instance.

## Definition of the route and DNS

## Use a security group with correct authorisation

For the moment I am using a predefined security group.

## Populating with Ansible

### Declaring the host

    vi /etc/ansible/hosts

    [jenkins]
        ubuntu@flub78.net

    [mina]
        ubuntu@ec2-13-39-105-56.eu-west-3.compute.amazonaws.com

### Test

A simple command

     ansible mina -m ping
        ubuntu@ec2-13-39-105-56.eu-west-3.compute.amazonaws.com | SUCCESS => {
            "ansible_facts": {
                "discovered_interpreter_python": "/usr/bin/python3"
            },
            "changed": false,
            "ping": "pong"
        }
And a simple playbook

    ansible-playbook test_connection.yml

ansible-playbook test_connection.yml

PLAY [Network Getting Started First Playbook] ***********************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [ubuntu@ec2-13-39-105-56.eu-west-3.compute.amazonaws.com]

TASK [test connection] **********************************************************************************************************************************************************************
ok: [ubuntu@ec2-13-39-105-56.eu-west-3.compute.amazonaws.com]

TASK [test root access] *********************************************************************************************************************************************************************
changed: [ubuntu@ec2-13-39-105-56.eu-west-3.compute.amazonaws.com]

PLAY RECAP **********************************************************************************************************************************************************************************
ubuntu@ec2-13-39-105-56.eu-west-3.compute.amazonaws.com : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0





    







    

