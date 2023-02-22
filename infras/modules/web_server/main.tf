resource "aws_instance" "app_server" {
  ami                    = var.ami
  instance_type          = var.instance_type
  vpc_security_group_ids = [var.vpc_sg_id]
  key_name               = var.key_name

  connection {
    type        = "ssh"
    user        = var.user
    private_key = file(var.private_key)
    host        = self.public_ip
  }

  tags = {
    Name = var.name
  }

  /*
   * Basic HTTP server for testing
   * It is not restarted on reboot
   */  
  user_data = <<-EOF
    #!/bin/bash
    echo "Hello, ${var.name} Flub78" > index.html
    python3 -m http.server 8888 &
  EOF
}