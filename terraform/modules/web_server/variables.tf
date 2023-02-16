variable "name" {
  description = "Basename for AWS resources"
  type        = string
  default     = "tf-web-server"
}

variable "ami" {
  description = "AMI ID for the web server"
  type        = string
}

variable "instance_type" {
  description = "Instance type for the web server"
  type        = string
}

variable "vpc_sg_id"  {
  description = "VPC security group ID for the web server"
}

variable key_name   {
  description = "Key name for the web server"
  type        = string
}

variable "user" {
  description = "User for the web server"
  type        = string
}

variable "private_key" {
  description = "Private key for the web server"
  type        = string
}