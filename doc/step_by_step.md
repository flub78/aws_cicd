# Step by step CI/CD Pipeline creation.

This is an example of creation and population of an EC2 instance.

## Creation of a key pair

## Creation of the instance

## SSH connection

### Association fo the instance with an elastic IP address

### Definition of the route and DNS

### Use a security group with correct authorisation

### ssh connection

## Ansible

### Ansible configuration

### Basic connection

### Populating the instance


## Creating an instance

    $ aws ec2 run-instances --image-id ami-0e019d7e4645e931d --count 1 --instance-type t2.micro --key-name cicd 
    
    $ aws  opsworks delete-instance \
    --region eu-west-3 \
    --instance-id i-00d73043bfb67240d

To create in instance I need:
* Security group ID
* Key pair name
* AMI ID
* Subnet ID


    
# connecting to an instance

Once an instance is up and running, it has been associated to a key pair and to a security group allowing ssh access it is possible to log on the instance.

    ssh -i ratus_ec2-keypair.pem ec2-user@ec2-35-180-138-100.eu-west-3.compute.amazonaws.com

    To connect to the instance using a domain name you need:
        - an AWS Elastic IP address must be associated to the instance
        - A S3 route to associate the domain and the the elastic IP address.

    once done it is possible to connect to the instance using the domain:

        ssh -i ratus_ec2-keypair.pem ubuntu@flub78.net hostname
            ip-172-31-32-114

## Installation of my public key to the managed nodes

    ssh-keygen -t rsa -b 4096 -C "frederic.peignot@free.fr"

    cat ~/.ssh/id_rsa.pub

    and copy it into .ssh/authorized_keys on the managed nodes

    it is then possible to type directly
        ssh ubuntu@flub78.net uptime






    

