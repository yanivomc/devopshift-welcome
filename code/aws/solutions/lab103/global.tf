provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-east-1"
}

variable "vm_name" {
  default = "vm-[YOURNAME]"
}

variable "admin_username" {
  default = "adminuser"
}

variable "admin_password" {
  default = "Password123!"
}

variable "vm_size" {
  default = "t2.micro"
}