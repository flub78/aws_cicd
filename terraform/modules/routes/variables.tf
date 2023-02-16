variable "server_id"  {
  description = "ID of the server to create a route for"
  type        = string
}

variable "basename" {
  description = "Basename for AWS resources"
  type        = string
  default     = "tf-mina"
}

variable "domain" {
  description = "Domain name for the web server"
  type        = string
  default     = "flub78.net"
}

variable "subdomain" {
  description = "Subdomain name for the web server"
  type        = string
  default     = "www"
}