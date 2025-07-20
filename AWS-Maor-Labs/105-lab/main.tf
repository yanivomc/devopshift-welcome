# resource "aws_vpc" "lab_vpc" {
#   cidr_block = "10.0.0.0/16"
#   enable_dns_support = true
#   enable_dns_hostnames = true

#   tags = {
#     Name = "Lab-VPC"
#   }
# }

# resource "aws_subnet" "public_subnet" {
#   vpc_id     = aws_vpc.lab_vpc.id
#   cidr_block = "10.0.1.0/24"
#   map_public_ip_on_launch = true
#   availability_zone = "us-east-1a"

#   tags = {
#     Name = "Public-Subnet"
#   }
# }

# resource "aws_subnet" "private_subnet" {
#   vpc_id     = aws_vpc.lab_vpc.id
#   cidr_block = "10.0.2.0/24"
#   availability_zone = "us-east-1a"

#   tags = {
#     Name = "Private-Subnet"
#   }
# }

# resource "aws_internet_gateway" "igw" {
#   vpc_id = aws_vpc.lab_vpc.id

#   tags = {
#     Name = "Lab-IGW"
#   }
# }


module "vpc" {
  source             = "./modules/vpc"
  vpc_cidr           = "10.0.0.0/16"
  public_subnet_cidr = "10.0.1.0/24"
}

module "ec2" {
  source        = "./modules/ec2"
  ami           = "ami-055e3d4f0bbeb5878"
  instance_type = "t2.micro"
  subnet_id     = module.vpc.public_subnet_id
}
