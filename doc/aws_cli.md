# AWS CLI

## Installation the version of a linux disttribution

    sudo apt-get update
    sudo apt install awscli

On WSL

    frederic@LAPTOP-57QER3OP:~$ aws --version
    aws-cli/1.22.34 Python/3.10.6 Linux/5.15.79.1-microsoft-standard-WSL2 botocore/1.23.34

On a linux Mint fanless machine

    frederic@pastille:~/cicd$ aws --version
    aws-cli/1.18.69 Python/3.6.9 Linux/4.15.0-54-generic botocore/1.16.19

## Installation of the latest version

    https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install

    $ aws --version
    aws-cli/2.11.3 Python/3.11.2 Linux/5.15.90.1-microsoft-standard-WSL2 exe/x86_64.ubuntu.22 prompt/off

## AWS CLI documentation

    https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#synopsis

# Initial step: Creation and Connection to an AWS EC2 instance.

It is the base, the scripts must be able to create and configure an EC2 instance and the user should be able to log on. Then more complex scripts can populate the EC2 instances.

## AWS CLI configuration

This is the way to configure the private information related to the AWS account.

These information must not be put under configuration.

Security Items are managed in the IAM service (Identity and Access Management).

    aws configure
    AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
    AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    Default region name [None]: us-west-3
    Default output format [None]: json

It is only possible to create two access keys for a user. You must delete one if you want to create another one. And the secrete key is only displayed during creation.

it is possible to manage several profiles with the option --profile

    $ aws configure --profile produser
    $ aws s3 ls --profile produser

## AWS CLI basic commands

    $ aws s3 ls
    $ aws ec2 describe-instances
    $ aws ec2 describe-key-pairs

## Troubleshooting

    https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-troubleshooting.html#general-debug

### Warning if the WSL date becomes out of sync with the current date AWS CLI can reject the credentials.

In this case type:

    sudo hwclock -s

