provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-east-1"
}

############# Get image ID
data "aws_ami" "terraformami" {
  owners = ["self"]
  filter {
    name = "name"
    values = ["terraform-workshop-image-do-not-delete"]
  }
  
}

data "aws_ami" "my-privateami" {
    owners = ["self"]  # Queries only AMIs owned by your account

}

output "yanivsami" {
  value = data.aws_ami.my-privateami
}

output "terraformimage" {
  value = data.aws_ami.terraformami.id
}


####
variable "vm_name" {
  default = "vm-yanivc"
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