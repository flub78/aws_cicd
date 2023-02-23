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
- [Terraform infrastructure provisioning](doc/terraform.md)
- [Ansible Playbooks and Roles](doc/ansible.md)
- [Jenkins](doc/jenkins.md)

## Some external tutorials

[Terraform Documentation](https://developer.hashicorp.com/terraform/docs)

[Ansible Documentation](https://docs.ansible.com/ansible/latest/index.html)

[Jenkins Documentation](https://www.jenkins.io/doc/)


https://courses.morethancertified.com/p/devops-in-the-cloud

https://www.devopsschool.com/blog/jenkins-commands-lines-reference-from-jenkins/

https://www.sfgroups.com/jenkins/pipeline/create_job_using_groovyscript/


## Videos

[Jenkins 30 tutos](https://www.youtube.com/playlist?list=PLn6POgpklwWr19VXuoVgIr32HCu0MGNt9)

[Tutorials et Formation Terraform](https://www.youtube.com/playlist?list=PLn6POgpklwWrpWnv05paAdqbFbV6gApHx)

[Formation Ansible](https://www.youtube.com/playlist?list=PLn6POgpklwWoCpLKOSw3mXCqbRocnhrh-)




