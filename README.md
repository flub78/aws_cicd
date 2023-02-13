# aws_cicd
A CI/CD pipeline for Laravel hosted on AWS

This project contains the scripts and information required to deploy a continuous integration, continuous delivery pipeline hosted on AWS. 

## Objective

The goal is to build a fully automated CI/CD pipeline. It should be possible with a few command to create the EC2 instances, to deploy a jenkins server, install and configure PHP, install a WEB server, then create the jenkins jobs to monitor a github project. When the github project is updated, the jenkins jobs should be triggered to run static code analysis, unit and integration tests, then deploy a fresh application and run the end to end tests on it. The process to deploy the application needs to be identical to the deployment of the application in production. Eventually the pipeline will also manage a long term application with dummy deployment data to perform update, robustness and performance tests.

Even for a personnal project a good CI/CD infrastructure is important. It is even more important when you have limited human resources to test and deploy your application. With a good test coverage and automated deployment it is possible for an individual developer to focus on writing the code and let the infrastructure test, validate and deploy the application.

I have spent quite a lot of time to develop this kind of infrastructure but they were only partially automated. So in case of hardware failures or data loses, I had to do a lot of manual work to recover. For example, I lost a key pair after a crash of my laptop and I lost the capacity to log on my EC2 instances.

The objective of this project is to build a fully automated CI/CD pipeline to validate Laravel or Android projects. Not only the application test and deployment had to be automatic once initialized, but also the creation of the test and validation infrastructure. In case of issues with my CI/CD pipeline I should be able to create a new one by running a few scripts. Even if these scripts become obsolete this project is a full documentation and it should be easy to update it and run it again.

The principle is infrastructure as code https://www.youtube.com/watch?v=POPP2WTJ8es

## Prerequisites

A control node to create an populate the infrastructure. It is typically a Linux machine, or a Windows Linux sub-system. Software required on the control node:

- [Terraform](doc/terraform.md)
- [Ansible](doc/ansible.md)
- [AWS CLI](doc/aws_cli.md) (tested with version 2)
- [python and boto3](doc/python_boto3.md)

## Table of content

- [Introduction](doc/introduction.md) 
- [CI/CD Architecture](doc/architecture.md)
- [AWS](doc/aws.md)
  
- [Step by step creation and population of an EC2 instance](doc/step_by_step.md)

- [Jenkins](doc/jenkins.md)
  - [https role](doc/https_role.md)
  - [mysql role](doc/mysql_role.md)




