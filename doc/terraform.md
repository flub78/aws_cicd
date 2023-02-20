# Terraform

## Installation

[https://developer.hashicorp.com/terraform/downloads

```
wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```

## Basic commands

```
$ tf -v
Terraform v1.3.8
```

```
$ terraform init
$ terraform fmt
$ terraform validate
$ terraform plan
$ terraform apply
$ terraform destroy
```

```
$ terraform state list
aws_instance.app_server
```

## Description of the infrastructure provisioning contexts

### infras/jenkins

Create a generic web server:
- an EC2 instance
- a key pair for ssh access
- a security groups with usual ports open
- an initial python web server
- an alarm to shut down unloaded instances
- a route to access the EC2 instance with a domain name
- a hosts file (ansible inventory)
- a file to setup environment variables used by ansible (ansible.setenv)