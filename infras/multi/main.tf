terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region = var.region
}

/* SSH key and security groups already exists
   so we don't need to create them again
*/

/*
module "ssh_key" {
  source = "../modules/ssh_key"
  basename = var.basename
  public_key = var.PUBLIC_KEY
}

module "sg" {
  source = "../modules/security_group"
  basename = var.basename
  # ingress_ports = var.ingress_ports
}
*/

data "aws_security_group" "sg" {
    name = "tf-ratus_sg"
}

module "webserver" {
  source = "../modules/web_server" 
  name = var.basename
  ami = var.ami
  instance_type = var.instance_type
  vpc_sg_id = data.aws_security_group.sg.id
  key_name = "tf-ratus_key"
  user = var.user
  private_key = file(var.PRIVATE_KEY)
}

module "routes" {
  source = "../modules/routes"
  basename = var.basename
  domain = var.domain
  subdomain = var.subdomain
  server_id = module.webserver.ec2.id
}

module "alarms" {
  source = "../modules/alarms"
  instance_id = module.webserver.ec2.id
}

resource "local_file" "hosts"{
  filename = "hosts"
  content = <<-EOF
  [${var.subdomain}]
      ${var.user}@${var.subdomain}.${var.domain}
  # [${var.subdomain}_ip]
  #     ${var.user}@${module.routes.elastic_ip.public_ip}
  EOF
}

resource "local_file" "ansible_setenv"{
  filename = "ansible.setenv"
  content = <<-EOF
  export INFRA_HOST=${var.subdomain}
  export INFRA_DOMAIN="${var.subdomain}.${var.domain}"
  EOF
}