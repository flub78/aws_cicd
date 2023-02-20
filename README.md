# aws_cicd
A CI/CD pipeline on AWS with terraform, ansible and jenkins for PHP Laravel and others projects.

## Objective

Full automation to deploy a jenkins server and several nodes for test and production.

The principles of infrastructure as code: https://www.youtube.com/watch?v=POPP2WTJ8es

## Prerequisites

A control node to create an populate the infrastructure. It is typically a Linux machine, or a Windows Linux sub-system. 

Software required on the control node:

- [Terraform](doc/terraform.md)
- [Ansible](doc/ansible.md)
- [AWS CLI](doc/aws_cli.md) (tested with version 2)
- [python and boto3](doc/python_boto3.md)

## Table of content

- [AWS](doc/aws.md)
- [CI/CD Pipeline description](doc/pipeline.md)
- [Step by step creation and population of an EC2 instance](doc/step_by_step.md)
- [Terraform infrastucture provisioning](doc/terraform.md)
- [Ansible Playbooks and Roles](doc/ansible.md)
- [Jenkins](doc/jenkins.md)




