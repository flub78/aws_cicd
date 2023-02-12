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
  region = "eu-west-3"
}

resource "aws_key_pair" "my_ec2" {
    key_name   = "tf-key"
    public_key = file(var.PUBLIC_KEY)
}

resource "aws_security_group" "tf_sg" {
    name = "terraform-test-sg"

    egress {
        from_port       = 0
        to_port         = 0
        protocol        = "-1"
        cidr_blocks     = ["0.0.0.0/0"]
    }

    ingress {
        from_port   = 80
        to_port     = 80
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_instance" "app_server" {
  ami           = "ami-0afd55c0c8a52973a"
  instance_type = "t2.medium"
  vpc_security_group_ids = [aws_security_group.tf_sg.id]
  key_name      = aws_key_pair.my_ec2.key_name

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file(var.PRIVATE_KEY)
        host        = self.public_ip
  }

  tags = {
    Name = var.instance_name
  }
}
