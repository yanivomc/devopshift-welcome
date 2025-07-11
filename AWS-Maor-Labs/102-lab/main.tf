
# Define Provider Configuration
provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-east-1"
}



#  Define a security group to allow SSH access to the VM
resource "aws_security_group" "sg-Maor" {
  
ingress {
    from_port   = 22
    to_port     = 22
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


#  create an EC2 instance
resource "aws_instance" "vm" {
  ami           = "ami-0c02fb55956c7d316" # Amazon Linux 2 AMI in us-east-1
  instance_type = "t2.micro"
  subnet_id = "subnet-06acd0b316280afeb"
  vpc_security_group_ids = [aws_security_group.sg-Maor.id]

  tags = {
    Name = "Maor-vm"
  }
}


resource "time_sleep" "wait_for_ip" {
  create_duration = "10s"  # Wait for 10 seconds
  depends_on = [ aws_instance.vm ]
}










