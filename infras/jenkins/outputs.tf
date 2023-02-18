output "instance" {
  description = "Instance data"
  value       = "${var.basename}    ${module.webserver.ec2.id}"
}

output "ssh_cmd" {
  description = "ssh command to login to the EC2 instance"
  value       = "ssh -i $TF_VAR_PRIVATE_KEY ubuntu@${module.routes.elastic_ip.public_dns}"
}

output "domain_ssh_cmd" {
  description = "ssh command to login to the EC2 instance"
  value       = "ssh -i $TF_VAR_PRIVATE_KEY ${var.user}@${var.subdomain}.${var.domain}"
}

output "http" {
  description = "url to access the app"
  value       = "http://${module.routes.elastic_ip.public_dns}:8080"
}

output "domain_http" {
  description = "url to access the app"
  value       = "http://${var.subdomain}.${var.domain}:8080"
}