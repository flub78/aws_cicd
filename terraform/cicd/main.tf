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


# resource block for elastic ip #
resource "aws_eip" "web_server_eip" {
  instance = module.webserver.ec2.id
  vpc      = true
    tags = {
    Name = "${var.basename}_eip"
  }
}

# resource block for route53 record #
data "aws_route53_zone" "primary" {
  name = "flub78.net"
  # name = var.domain
}

resource "aws_route53_record" "root" {
  zone_id = data.aws_route53_zone.primary.zone_id
  name    = var.domain
  type    = "A"

  ttl    = "300"
  records = [aws_eip.web_server_eip.public_ip]
}
