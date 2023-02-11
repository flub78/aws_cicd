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
    key_name   = "terraform-key"
    public_key = file(".ssh/terraform.pub")
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
  instance_type = "t2.nano"
  vpc_security_group_ids = [aws_security_group.tf_sg.id]
  key_name      = aws_key_pair.my_ec2.key_name

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file(".ssh/terraform")
        host        = self.public_ip
  }

  provisioner "remote-exec" {
    inline = [
          "sudo apt-get -f -y update",
          "sudo apt-get install -f -y apache2",
          "sudo systemctl start apache2",
          "sudo systemctl enable apache2",
          "sudo sh -c 'echo \"<h1>Hello devopssec</h1>\" > /var/www/html/index.html'",
    ]
  } 

  tags = {
    Name = var.instance_name
  }
}
