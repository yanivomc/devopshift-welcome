# VARIABLES
variable "instance_count" {
  description = "Number of EC2 instances to create"
  default     = 2
}

variable "region" {
  default     = "us-west-2"
  description = "AWS Region"
}



variable "ami" {
  default = "ami-04feae287ec8b0244"
  
}
variable "vm_name" {
  default = "vm-yaniv"
}

variable "admin_username" {
  default = "admin-user"
}

variable "admin_password" {
  default = "Password123!"
}

variable "vm_size" {
  default = "t2.micro"
}
# *********

# PROVIDER
provider "aws" {
  region = var.region
}