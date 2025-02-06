variable "create_vpc" {
 type    = bool
 default = false
}

variable "create_ec2" {
 type    = bool
 default = true
}

variable "myname" {}


# Create VPC only if enabled
resource "aws_vpc" "custom_vpc" {
 count = var.create_vpc ? 1 : 0

 cidr_block           = "10.0.0.0/16"
 enable_dns_support   = true
 enable_dns_hostnames = true

 tags = {
   Name = "${var.myname}-vpc"
 }
}

# Create subnet inside the VPC
resource "aws_subnet" "custom_subnet" {
 count = var.create_vpc ? 1 : 0

 vpc_id            = aws_vpc.custom_vpc[0].id
 cidr_block        = "10.0.1.0/24"
 map_public_ip_on_launch = true

 tags = {
   Name = "${var.myname}-subnet"
 }
}

# Get default VPC and default subnet if custom VPC is not created
data "aws_vpc" "default" {
 default = true
}


variable "az_list" {
 default = ["us-east-1a","us-east-1b","us-east-1c"]
}

resource "random_shuffle" "random_az" {
  input        = var.az_list
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




# EC2 Instance
resource "aws_instance" "example" {
 count = var.create_ec2 ? 1 : 0

 ami           = "ami-0c02fb55956c7d316" # Ubuntu AMI
 instance_type = "t2.micro"

 subnet_id = var.create_vpc ? aws_subnet.custom_subnet[0].id : data.aws_subnet.default.id

 associate_public_ip_address = var.create_vpc ? true : false

 tags = {
   Name = "${var.myname}-ec2"
 }

 # FIX: Conditional dependency to avoid issues (DONT FOR GET TO TALK ABOUT THIS)
 lifecycle {
   ignore_changes = [subnet_id]
 }
}

# OUTPUTS
output "ec2_public_ip" {
 value = var.create_ec2 ? aws_instance.example[0].public_ip : "No EC2 instance was created"
}

output "vpc_subnet_info" {
 value = var.create_vpc ? "The following is your VPC: ${aws_vpc.custom_vpc[0].id} and Subnet: ${aws_subnet.custom_subnet[0].id}" : "Using default VPC (${data.aws_vpc.default.id}) and Subnet (${data.aws_subnet.default.id})"
}




