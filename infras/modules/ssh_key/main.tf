resource "aws_key_pair" "ssh_kp" {
  key_name   = "${var.basename}_key"
  public_key = file(var.public_key)
}
