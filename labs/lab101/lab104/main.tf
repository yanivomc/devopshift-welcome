variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "YOURNAME" {
  type = string
  default = "yovel"
}

variable "create_vpc" {
  type    = bool
  default = false
}

variable "create_ec2" {
  type    = bool
  default = true
}

provider "aws" {
  region = var.aws_region
}

resource "aws_vpc" "custom_vpc" {
  count = var.create_vpc ? 1 : 0

  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "${var.YOURNAME}-vpc"
  }
}

resource "aws_subnet" "custom_subnet" {
  count = var.create_vpc ? 1 : 0

  vpc_id                 = aws_vpc.custom_vpc[0].id
  cidr_block             = "10.0.1.0/24"
  map_public_ip_on_launch = true

  tags = {
    Name = "${var.YOURNAME}-subnet"
  }
}
variable "az" {
  default = ["us-east-1a", "us-east-1b", "us-east-1c"]
}
resource "random_shuffle" "random_az" {
  input = var.az
  result_count = 1
}

data "aws_subnet" "default" {
  filter {
    name   = "default-for-az"
    values = ["true"]
  }

  filter {
    name   = "availability-zone"
    values = [random_shuffle.random_az.result[0]]
}
}
resource "aws_instance" "example" {
  count = var.create_ec2 ? 1 : 0

  ami           = "ami-0ecc0e0d5986a576d"
  instance_type = "t2.micro"

  associate_public_ip_address = true  

  subnet_id = var.create_vpc ? aws_subnet.custom_subnet[0].id : data.aws_subnet.default.id

  tags = {
    Name = "${var.YOURNAME}-ec2"
  }

  depends_on = [aws_vpc.custom_vpc]
}
output "instance_ip" {
  value       = var.create_ec2 ? aws_instance.example[0].public_ip : "No instance created"
 
}
