/*
 * Resource names
 */  

variable "basename" {
  description = "Basename for AWS resources"
  type        = string
  default     = "tf-mina"
}

/*
 * Infrastructure configuration
 */ 
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

variable "region" {
  description = "AWS region to use"
  type        = string
  default     = "eu-west-3"
}

variable "ami" {
  description = "AWS ami for EC2 instance"
  type        = string
  default     = "ami-0afd55c0c8a52973a" # Ubuntu 22.04 LTS
}

variable "instance_type" {
  description = "AWS EC2 instance type"
  type        = string
  default     = "t2.medium"
}

variable "user" {
  description = "User to use for the EC2 instance"
  type        = string
  default     = "ubuntu"
  sensitive   = true
}

variable "domain" {
  description = "Domain name to use for the EC2 instance"
  type        = string
  default     = "flub78.net"
}