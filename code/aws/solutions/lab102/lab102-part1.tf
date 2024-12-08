terraform {
  required_providers {
    time = {
      source = "hashicorp/time"
      version = "0.7.2"  # Ensure you're using the latest version
    }
  }
}
provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-east-1"
}

resource "aws_security_group" "sg" {
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

resource "aws_instance" "vm" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.sg.id]

  tags = {
    Name = "[YOURNAME]-vm"
  }
}


resource "time_sleep" "wait_for_ip" {
  create_duration = "30s"  # Wait for 30 seconds to allow Azure to allocate the IP
}


output "vm_public_ip" {
  value       = aws_instance.vm.public_ip
  depends_on  = [time_sleep.wait_for_ip]  # Wait for the time_sleep resource to complete
  description = "Public IP address of the VM"
}

