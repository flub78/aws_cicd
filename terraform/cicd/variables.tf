variable "instance_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "tf-mina"
}

variable "PUBLIC_KEY" {
  description = "Path to the public key to use for the EC2 instance"
  type        = string
  default     = "~/.ssh/id_rsa.pub"
}

variable "PRIVATE_KEY" {
  description = "Path to the private key to use for the EC2 instance"
  type        = string
  default     = "~/.ssh/id_rsa"
}

