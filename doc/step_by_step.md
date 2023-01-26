# Step by step CI/CD Pipeline creation.

My previous CI/CD pipeline being no more usable, it is an opportunity to start again from scratch with the objective to get a fully automated Continuous Integration, Continuous Deployment Pipeline.

Depending on the projects variations are possible. The pipeline may be different to integrate a javascript, an Android or a PHP project. The goal is to develop a set of scripts that can be called from a main one to create a pipeline. The process can be tuned by a minimal set of environment variables (the git repo, a deployment or test domain, an instance name). I really want to be able to launch a script and get the full deployment without manual intervention.

## Typical deployment.

The first project to be integrated will be a continuous test and integration environment for a PHP Laravel project. This setup should be usable on others type of project just by changing the environment variables and the list of steps to perform.

## The control machine

It is the machine on which this git project is checked out and the scripts to create the CI/CD pipeline are executed.

It is important to have the minimal set of requirements on this machine. Typically I may want a Linux shell, may be an ansible or aws CLI environment but nothing more. In particular the setting of this machine must be really simple compared to the setting of the deployed pipeline.

If possible it should work on old Linux machine or limited environments like Raspberry PI or Windows WSL.

## Tools and Technologies



### Ansible

    sudo apt-get update
    sudo apt install ansible-core

    ansible --version
    ansible [core 2.12.0]
        config file = None
        configured module search path = ['/home/frederic/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
        ansible python module location = /usr/lib/python3/dist-packages/ansible
        ansible collection location = /home/frederic/.ansible/collections:/usr/share/ansible/collections
        executable location = /usr/bin/ansible
        python version = 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0]
        jinja version = 3.0.3
        libyaml = True

#### First communication with an EC2 instance

create the file /etc/ansible/hosts on the control host

and fill it
cat /etc/ansible/hosts
[jenkins]
        ubuntu@flub78.net

ansible all -m ping
ubuntu@flub78.net | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}

# Architecture

## Definitions

* Deployment: it is the set of all ressources required to provide one or several services. It may contain virtual networks, security keys, ec2 instances, etc. Two deployments may belong to different organization and they should not share resources.
* Deployment sub-system, it is the set or resources used to provide a service inside a deployment. For example a jenkins server, a test server or a production system. A subsystem can have dependencies or knowledge about other sub-systems. For example a jenkins server can interact with a virtual machine under test. Inside a deployment sub-systems can share resources, for example they can be inside the same VPC.
* Deployment components are the basic block of deployment or sub-system.

## Conventions

It may be convenient to apply the following naming convention:

* deployment: strings without dashes
* subs-systems: DeploymentName-SubSystemName (two strings dash separated)
* components: DeploymentName-SubSystem-Component or DeploymentName-Component (depending if the component is specific to a subsystem or not). To only have one format, it is possible to define a subsystem named "global".

It may also be convenient to add a string to define the type of the ID like, keypair, vpc, ec2instance, etc... (to be checked but it looks that AWS already enforce that sg-0b864f5c5c2ceb714, vpc-b615dbdf)

Note that this convention is only an option, it is possible to let the scripts create resources and use the random IDs returned by AWS but it will make the debugging and manual checking of the deployments much harder.

## Cost considerations

AWS bills you on the number of resources that you use and create. To optimize the costs, it may make sense to share some resources (for example to have only one virutal network for a team). So the scripts must be able to create all the components of a deployment but also to reuse existing one.

## Possible actions

The scripts must be able to create, run, restart, suspend or delete a deployment, a sub-system or a component.
* Create should create the create the required components
* Run should pass all component in active state
* Suspend or pause, should put them in a state that minimize billing
* Delete should erase the components for good. Note that pre-existing components should not be deleted. A full set of scripts should contains scripts to manage components and sub-systems. Every script should be in charge of a sub-system or component and should be the only way to create or delete the resources (just to avoid side effect of components deleted by a script which has not created them).

So the scripts should all have the same structrure:

    script_level type action id options
    script_level = dep, sub or comp for deployment, sub-system or component

    type:
        * for deployment describe the type of deployments that the scripts can handle example, the name of a laravel project, or an android project, etc.
        * for the subsystem, it identifies the type of subsystem, for example test_server, jenkins server, production env, etc.
        * for components, it identifies the type of component, vpc, ec2, key_pair, etc.

    actions: create, run, suspend, delete, list, ect.

    ID : ID of the entity to create or handle, optional for some commands like list.

    Options may describe some share resources or others options.

* dep type create id
* sub 

# Initial step: Creation and Connection to an AWS EC2 instance.

It is the base, the scripts must be able to create and configure an EC2 instance and the user should be able to log on. Then more complex scripts can populate the EC2 instances.

## AWS CLI configuration

This is the way to configure the private information related to the AWS account.

These information must not be put under configuration.

Security Items are managed in the IAM service (Identity and Access Management).

    aws configure
    AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
    AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    Default region name [None]: us-west-2
    Default output format [None]: json

It is only possible to create two access keys for a user. You must delete one if you want to create another one. And the secrete key is only displayed during creation.

it is possible to manage several profiles with the option --profile

    $ aws configure --profile produser
    $ aws s3 ls --profile produser

## AWS CLI basic commands

    $ aws s3 ls
    $ aws ec2 describe-instances
    $ aws ec2 describe-key-pairs

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

# Using python with AWS

## Installation

    pip install awscli boto3

    if Command 'pip' not found, but can be installed with:
    sudo apt install python3-pip

    Create a User and get AWS Access ID and Secret Key

## Python scripts

    aws.py          a template with the most usual parameters
    key_pair.py     manages key pairs
    ec2.py          manages ec2 instances
    
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






    

