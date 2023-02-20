# Using python with AWS

For convenience, there are some python scripts to manage AWS resources. I initially intended to use them to provision the infrastructure but it is easier whith terraform.

These scripts have not all been finished and they will only be completed if the become used in the pipeline. Until then use them with caution.

## Installation

    pip install awscli boto3

    if Command 'pip' not found, but can be installed with:
    sudo apt install python3-pip

    Create a User and get AWS Access ID and Secret Key

## Python scripts

    aws.py          a template with the most usual parameters
    key_pair.py     manages the AWS key pairs
    ec2.py          manages the AWS ec2 instances
    alarm.py        alarms management