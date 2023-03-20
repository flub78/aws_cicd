/**
  * Main terraform script to create an EC2 machine for GVV testing
  *
  */

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

# a route for the application
# resource block for route53 record #
data "aws_route53_zone" "primary" {
  name = var.domain
}

# data "aws_eip" "web_server_eip" {
#   tags = {
#     Name = "${var.basename}_eip"
#   }
# }

resource "aws_route53_record" "root" {
  zone_id = data.aws_route53_zone.primary.zone_id
  name    = "webapp.${var.subdomain}.${var.domain}"
  type    = "A"
  ttl    = "300"
  records = [module.routes.elastic_ip.public_ip]
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