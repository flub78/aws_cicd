# Introduction

## Typical deployment.

The first project to be integrated is a continuous test and integration environment for a PHP Laravel project. This setup should be usable on others type of project just by modifying the infrastructure provisioning and the list of roles to apply.

# Architecture

## Pipeline creation steps

- Infrastucture provisioning. A set of Terraform configurations will be used to create AWS resources (vpc, security groups, key pairs, EC2 instances, etc.). Once the infrastructure is provisioned it is possible to access EC2 instances with ssh and so to execute ansible scripts.

- Infrastructure configuration. Once the resources are created, a set of ansible script can be used to install software on the machine, create jenkins jobs, etc. The idea is to have hierarchical scripts to specialize the instances.

- Python scripts provides a convenient way to get information on the deployed infrastructure, stop and resume the instances, etc.


### Example

1. First an EC2 instance is created with its environment
1. Then LAMP is installed on the instance
1. Then phpmyadmin is installed
1. Then jenkins and PHP tools
1. Then Laravel jenkins jobs are installed

or 
1. First an EC2 instance is created with its environment
1. Then LAMP is installed on the instance
1. Then application in development is installed

## Directory structure

Except for the inventory, ansible scripts are generic and can be applied to a lot of deployment.

Terraform configuration are specific to one deployement. Each terraform configuration directory should contain a setenv.sh script to setup the environment variables common to terraform and ansible.

To manage an infrastructure:

1. cd to the terraform configuration directory
1. setup the environment variables
1. terraform apply
1. cd to the ansible playbook directory
1. apply the playbooks required to the infrastructure.
1. use the python scripts to monitor, enable and disable part of the infrastucture.

## Terraform Ansible communication

With terraform it is possible to manage similar but different infrastucture with directory structure, workspaces and tfvars files.

To keep things simple, I'd really would like to fully manage an infrastucture from a single directory. This directory would contain eveything specific to one deployment and every terraform command or ansible playbook should apply to it.

## Cost considerations

AWS bills you on the number of resources that you use and create. To optimize the costs, it may make sense to share some resources (for example to have only one virutal network for a team). So the scripts must be able to create all the components of a deployment but also to reuse existing one.

## Python scripts

My initial intend was to manage all the infrastucture with python scripts but I decided to use terraform instead.

There still some python scripts in this project, they are able
to monitor or manage the AWS resources from the linux command line. So far I have a script to manage the EC2 instances, key pairs, alarms, etc.

Each script is able to list, create and delete resources. The ec2.py can also stop or restart an instance.

