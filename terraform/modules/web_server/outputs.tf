output "ec2" {
  description = "The EC2 instance"
  value       = aws_instance.app_server
}