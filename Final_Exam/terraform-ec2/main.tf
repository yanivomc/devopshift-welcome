provider "aws" {
  region = "us-east-1"
}
resource "tls_private_key" "ssh_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}
resource "local_file" "private_key" {
  content         = tls_private_key.ssh_key.private_key_pem
  filename        = "${path.module}/builder_key.pem"
  file_permission = "0600"
}
resource "aws_key_pair" "builder_key" {
  key_name   = "yaniv-roticsfe-key"
  public_key = tls_private_key.ssh_key.public_key_openssh
}
resource "aws_security_group" "builder_sg" {
  name        = "yaniv-roticsfe-sg"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["54.202.56.153/32"]
  }
  ingress {
    from_port   = 5001
    to_port     = 5001
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
    # for jenkins
  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
resource "aws_subnet" "main" {
  vpc_id                  = "vpc-044604d0bfb707142"
  cidr_block              = "172.31.144.0/20"
  map_public_ip_on_launch = true
  
  tags = {
    Name = "yaniv-roticsfe-subnet"
  }
}
resource "aws_route_table" "main" {
  vpc_id = "vpc-044604d0bfb707142"
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "igw-0c3d8c45c5bd39e34"
  }
  
  tags = {
    Name = "yaniv-roticsfe-route-table"
  }
}
resource "aws_route_table_association" "main" {
  subnet_id      = aws_subnet.main.id
  route_table_id = aws_route_table.main.id
}
data "aws_ssm_parameter" "ubuntu_ami" {
  name = "/aws/service/canonical/ubuntu/server/20.04/stable/current/amd64/hvm/ebs-gp2/ami-id"
}
resource "aws_instance" "builder" {
  ami                    = data.aws_ssm_parameter.ubuntu_ami.value
  instance_type          = "t3.medium"
  key_name               = aws_key_pair.builder_key.key_name
  vpc_security_group_ids = [aws_security_group.builder_sg.id]
  subnet_id              = aws_subnet.main.id
  associate_public_ip_address = true

  tags = {
    Name = "builder"
  }
}
output "instance_public_ip" {
  value = aws_instance.builder.public_ip
}
output "ssh_private_key_path" {
  value       = local_file.private_key.filename
  description = "Path to the generated private SSH key"
  sensitive   = true
}
output "security_group_id" {
  value = aws_security_group.builder_sg.id
}