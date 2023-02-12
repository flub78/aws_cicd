# AWS CI/CD pipeline

## Table of Content

## Introduction

Even for a personnal project a good CI/CD infrastructure is important. It is even more important when you have limited human resources to test and deploy your application. With a good test coverage and automated deployment it is possible for an individual developer to focus on writing the code and let the infrastructure test, validate and deploy the application.

I have spent quite a lot of time to develop this kind of infrastructure but they were only partially automated. So in case of hardware failures or data loses, I had to do a lot of manual work to recover. For example, I lost a key pair after a crash of my laptop and I lost the capacity to log on my EC2 instances.

The objective of this project is to build a fully automated CI/CD pipeline to validate Laravel or Android projects. Not only the application test and deployment had to be automatic once initialized, but also the creation of the test and validation infrastructure. In case of issues with my CI/CD pipeline I should be able to create a new one by running a few scripts. Even if these scripts become obsolete this project is a full documentation and it should be easy to update it and run it again.

The principle is infrastructure as code https://www.youtube.com/watch?v=POPP2WTJ8es

## Table of content

- [Introduction](introduction.md) 
- [CI/CD Architecture](architecture.md)
- [Tools](tools.md)
  
- AWS
  - [AWS CLI](aws_cli.md)
  - [Using Python and boto3 to manage AWS objects](python_boto3.md)

- [Terraform](terraform.md)

- [Ansible](ansible.md)

- [Step by step creation and population of an EC2 instance](step_by_step.md)

- [Jenkins](jenkins.md)
  - [https role](https_role.md)
  - [mysql role](mysql_role.md)

