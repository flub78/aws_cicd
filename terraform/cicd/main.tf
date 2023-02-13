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

resource "aws_key_pair" "tf_mina_kp" {
  key_name   = "tf-mina_key"
  public_key = file(var.PUBLIC_KEY)
}

resource "aws_security_group" "tf_mina_sg" {
  name = "tf-mina-sg"

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
  ami                    = "ami-0afd55c0c8a52973a"
  instance_type          = "t2.medium"
  vpc_security_group_ids = [aws_security_group.tf_mina_sg.id]
  key_name               = aws_key_pair.tf_mina_kp.key_name

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file(var.PRIVATE_KEY)
    host        = self.public_ip
  }

  tags = {
    Name = var.instance_name
  }

  user_data = <<-EOF
    #!/bin/bash
    echo "Hello, Flub78" > index.html
    python3 -m http.server 8080 &
  EOF
}
