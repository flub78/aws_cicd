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

### AWS CLI

#### Installation the version of a linux disttribution

    sudo apt-get update
    sudo apt install awscli

On WSL
    frederic@LAPTOP-57QER3OP:~$ aws --version
    aws-cli/1.22.34 Python/3.10.6 Linux/5.15.79.1-microsoft-standard-WSL2 botocore/1.23.34

On pastille

    frederic@pastille:~/cicd$ aws --version
    aws-cli/1.18.69 Python/3.6.9 Linux/4.15.0-54-generic botocore/1.16.19

#### Installation of the latest version

    https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

### Ansible

## Initial step Creation and Connection to an AWS EC2 instance.

It is the base, the scripts must be able to create and configure an EC2 instance and the user should be able to log on. Then more complex scripts can populate the EC2 instances.

### AWS CLI configuration

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

### AWS CLI basic commands

    aws s3 ls
    

