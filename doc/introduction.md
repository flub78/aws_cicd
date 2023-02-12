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

1. cd to the terraform related configuration directory
1. setup the environment variables
1. terraform apply
1. cd to the ansible playbook directory
1. apply the playbooks required to the infrastructure.
1. use the python scripts to monitor, enable and disable part of the infrastucture.

## Cost considerations

AWS bills you on the number of resources that you use and create. To optimize the costs, it may make sense to share some resources (for example to have only one virutal network for a team). So the scripts must be able to create all the components of a deployment but also to reuse existing one.

## Python scripts

The scripts are able to restart, suspend or delete a deployment, a sub-system or a component.

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

