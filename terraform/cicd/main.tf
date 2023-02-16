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

module "webserver" {
  source = "../modules/web_server" 
  name = "${var.basename}_webserver"
  ami = var.ami
  instance_type = var.instance_type
  vpc_sg_id = module.sg.security_group.id
  key_name = module.ssh_key.key_pair.key_name
  user = var.user
  private_key = file(var.PRIVATE_KEY)
}

module "routes" {
  source = "../modules/routes"
  basename = var.basename
  domain = var.domain
  subdomain = "web"
  server_id = module.webserver.ec2.id
}
