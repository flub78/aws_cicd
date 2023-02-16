output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.app_server.id
}

/*
output "elastic_ip" {
  description = "Elastic IP"
  value       = aws_eip.web_server_eip.public_ip
}
*/

output "domain" {
  description = "Domain name"
  value       = var.domain
}

output "instance_ssh_cmd" {
  description = "ssh command to login to the EC2 instance"
  value       = "ssh -i $TF_VAR_PRIVATE_KEY ubuntu@${aws_eip.web_server_eip.public_dns}"
}

output "http" {
  description = "url to access the app"
  value       = "http://${aws_eip.web_server_eip.public_dns}:8080"
}