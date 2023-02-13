output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.app_server.id
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.app_server.public_ip
}

output "instance_public_dns" {
  description = "Public DNS of the EC2 instance"
  value       = aws_instance.app_server.public_dns
}

output "instance_ssh_cmd" {
  description = "ssh command to login to the EC2 instance"
  value       = "ssh -i $TF_VAR_PRIVATE_KEY ubuntu@${aws_instance.app_server.public_dns}"
}