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

# Create an AWS key pair using the public key
resource "aws_key_pair" "builder_key" {
  key_name   = "builder-key"
  public_key = tls_private_key.ssh_key.public_key_openssh
}

# Create a security group
resource "aws_security_group" "builder_sg" {
  name        = "builder-sg"
  description = "Security group for the EC2 builder instance"

  # Allow SSH from your IP (Replace YOUR_IP with actual IP)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["YOUR_IP/32"]
  }

  # Allow HTTP on port 5001 (for Python app)
  ingress {
    from_port   = 5001
    to_port     = 5001
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create an EC2 instance
resource "aws_instance" "builder" {
  ami                    = "ami-0c55b159cbfafe1f0"  # Ubuntu 22.04 LTS (Ensure this is available in us-east-1)
  instance_type          = "t3.medium"
  key_name               = aws_key_pair.builder_key.key_name
  vpc_security_group_ids = [aws_security_group.builder_sg.id]
  subnet_id              = "subnet-XXXXXXXXXXXX"  # Replace with a public subnet in VPC vpc-044604d0bfb707142
  associate_public_ip_address = true

  tags = {
    Name = "builder"
  }
}

# Outputs
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
