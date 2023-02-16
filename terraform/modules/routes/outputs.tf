output "elastic_ip" {
  description = "Eleastic IP for the EC2 instance"
  value       = aws_eip.web_server_eip
}