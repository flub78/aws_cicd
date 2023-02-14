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

resource "aws_key_pair" "ssh_kp" {
  key_name   = "${var.basename}_key"
  public_key = file(var.PUBLIC_KEY)
}

resource "aws_security_group" "webapp_sg" {
  name = "${var.basename}_sg"

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "app_server" {
  ami                    = var.ami
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.webapp_sg.id]
  key_name               = aws_key_pair.ssh_kp.key_name

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

resource "aws_route53_zone" "primary" {
  name = var.domain
}

resource "aws_route53_record" "root" {
  zone_id = aws_route53_zone.primary.zone_id
  name    = var.domain
  type    = "A"

  ttl    = "300"
  records = [aws_eip.web_server_eip.public_ip]
}
