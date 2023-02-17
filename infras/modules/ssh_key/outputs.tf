output "key_pair" {
  description = "The AWS key pair"
  value       = aws_key_pair.ssh_kp
}