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

resource "aws_instance" "app_server" {
  ami                    = var.ami
  instance_type          = var.instance_type
  vpc_security_group_ids = [module.sg.security_group.id]
  key_name               = module.ssh_key.key_pair.key_name

  connection {
    type        = "ssh"
    user        = var.user
    private_key = file(var.PRIVATE_KEY)
    host        = self.public_ip
  }

  tags = {
    Name = "${var.basename}_app_server"
  }

  user_data = <<-EOF
    #!/bin/bash
    echo "Hello, ${var.basename} Flub78" > index.html
    python3 -m http.server 8080 &
  EOF
}

# resource block for elastic ip #
resource "aws_eip" "web_server_eip" {
  instance = aws_instance.app_server.id
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
