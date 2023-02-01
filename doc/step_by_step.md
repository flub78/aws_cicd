# Step by step CI/CD Pipeline creation.

This is an example of creation and population of an EC2 instance.

## Pre-conditions

Even if the goa is to become 100 % automated and scripted, the first version of this script will be base on the following assumption.

- the AMI is hardcoded in the script
- there is an existing security group allowing ssh access and HTTP and HTTPS requests


## Creation of a key pair

    ./key_pair.py -v -c --name mina_keypair

This create the keypair in the cloud and store the private key in a file named mina_keypair.pem

The existing keys can be listed with

    ./key_pair.py -l

    frederic@LAPTOP-57QER3OP:~/aws_cicd/python$ ./key_pair.py -l
        JenkinsKeyPair key-0ab43bc7c2096e6f4 rsa
        jenkins_key_pair2 key-06bf11f5bdc28feeb rsa
        cicd key-0d57982c1856230ee rsa
        ratus_ec2-keypair key-0b76bf8ab760d67f6 rsa

And later the key can be deleted with 

    ./key_pair.py -d -n mina_keypair

## Creation of the instance

    ./ec2.py --create --name ratus_mina -v --key ratus_ec2-keypair

    ./ec2.py -l
        aws_jenkins_3 i-006e41d406f18df82 ami-06d79c60d7454e2af t2.small stopped eu-west-3c
        i-0f438540903311d62 ami-0e019d7e4645e931d t2.micro stopped eu-west-3c
        ratus_ec2-i i-0f1ec6a0bc9c090cc ami-0afd55c0c8a52973a t2.micro running eu-west-3c ec2-15-188-12-157.eu-west-3.compute.amazonaws.com
        ratus_mina i-05f38e34e76c7e603 ami-0afd55c0c8a52973a t2.micro running eu-west-3c ec2-15-188-53-68.eu-west-3.compute.amazonaws.com

Once no more needed the instance can be deleted

    ./ec2.py -v -d -i i-05f38e34e76c7e603

## SSH connection

Once the instance is up and running it is possible to login using the default user and DNS address.

    ssh  -i ratus_ec2-keypair.pem ubuntu@ec2-13-39-105-56.eu-west-3.compute.amazonaws.com

    https://linuxbeast.com/tutorials/aws/ssh-without-password-on-linux-amazon-ec2-ubuntu/

    It is also possible to copy my public key in the instance to allow ssh without having to specify a key.
 
    cat ~/.ssh/id_rsa.pub | sudo ssh -i ratus_ec2-keypair.pem ubuntu@ec2-13-39-105-56.eu-west-3.compute.amazonaws.com "cat >> /home/ubuntu/.ssh/authorized_keys"

    ssh ubuntu@ec2-13-39-105-56.eu-west-3.compute.amazonaws.com

## Creation of an alarm for automatic shutdown

As EC2 instances can be pretty expensive it is useful to have them automatically stopping when they are not used.
Currently it can be done from the AWS console, by clicking on the cross close to "Alarm status"

## Association fo the instance with an elastic IP address

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





    







    

