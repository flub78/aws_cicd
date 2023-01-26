# AWS CI/CD pipeline

## Table of Content

## Introduction

Even for a personnal project a good CI/CD infrastructure is important. It is maybe even more important when you have limited human resources to test and deploy your application. With a good test coverage and automated deployment it is possible for an individual developer to focus on writing the code and let the infrastructure test, validate and deploy the application.

I have spent quite a lot of time to develop these infrastructure but even if partially automated my previous realisations were not fully robust against hardware failures or loses of data. I lost a key pair after a crash of my laptop and I lost several validation environments when my small fanless linux machine decided to not boot anymore.

So the objective of this project is to build a fully automated CI/CD pipeline able to validate Laravel or ANdroid projects. Not only the application test and deployment had to be automatic once initialized, but the creation of the test and validation infrastructure has to be automatic. So in case of issues with my CI/CD pipeline I should be able to create a new one with just one command. Even if these scripts become obsolete this project is a full documentation and it should be easy to update it and start again.

The technologies chosen for that are:
* AWS to deploy virtual machines and virtual networks
* Python 3 and boto3 to manage AWS object from a set of scripts
* ansible to populate the virtual machines
* jenkins as automation server https://www.jenkins.io/
* github to manage the scripts

Of course these tools make sense in 2023, but maybe that they will be replaced in the futur by more convenient ones. It is the CI/CD spirit which is important, not the tools.

The principle is config as code https://www.octopus.com/blog/config-as-code-what-is-it-how-is-it-beneficial. 

## Table of content

- AWS
  - [AWS CLI](aws_cli.md)
  - [Using Python and boto3 to manage AWS objects](python_boto3.md)

- [Ansible](ansible.md) 