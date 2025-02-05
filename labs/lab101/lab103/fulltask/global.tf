provider "aws" {
 region = var.region
}

variable "region" {
 default = "us-east-1"
}

data "aws_ami" "terrformami" {
  owners = [ "self" ]
  filter {
    name = "name"
    values = ["terraform-workshop-image-do-not-delete"]
  }
}
output "findmyAmi" {
    value = data.aws_ami.terrformami.id
  
}


# data "aws_ami" "my-privateami" {
#   owners = [ "self" ]
# }

# output "yanivsami" {
#   value = data.aws_ami.my-privateami
# }


variable "vm_name" {
 default = "vm-yovel"
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