output "instance_id" {
  description = "ID of the EC2 instance"
  # value       = aws_instance.app_server.id
  value       = module.webserver.ec2.id
}

output "domain" {
  description = "Domain name"
  value       = var.domain
}

output "instance_ssh_cmd" {
  description = "ssh command to login to the EC2 instance"
  value       = "ssh -i $TF_VAR_PRIVATE_KEY ubuntu@${module.routes.elastic_ip.public_dns}"
}

output "http" {
  description = "url to access the app"
  value       = "http://${module.routes.elastic_ip.public_dns}:8080"
}