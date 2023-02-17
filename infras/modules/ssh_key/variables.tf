variable "basename" {
  description = "Basename for AWS resources"
  type        = string
  default     = "tf-mina"
}

variable "public_key" {
  description = "Path to the public key to use for the EC2 instance"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
}