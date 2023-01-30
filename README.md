# aws_cicd
A CI/CD pipeline for Laravel hosted on AWS

This project contains the scripts and information required to deploy a continuous integration, continuous delivery pipeline hosted on AWS. 

The ultime goal is to get it fully automated, it should be possible from a single script to create the EC2 instances, to deploy a jenkins server, install and configure PHP, install a WEB server, then create the jenkins jobs to monitor a github project. When the github project is updated, the jenkins jobs should be triggered to run static code analysis, unit and integration tests, then deploy a fresh application and run the end to end tests on it. The process to deploy the application needs to be identical to the deployment of the application in production. Eventually the pipeline will also manage a long term application with dummy deployment data to perform update, robustness and performance tests.


## Prerequisites

- a control node to create an populate the infrastructure. It is typically a Linux machine, or the Windows Linux sub-system.
- Ansible installed on this machine
- AWS cli, installed on this machine (tested with version 2)
- python and boto3 installed on the control node.

## Getting started

- [AWS CI/CD pipeline](doc/aws_cicd_pipeline.md)
- [Step by step CI/CD Pipeline creation](doc/step_by_step.md)


