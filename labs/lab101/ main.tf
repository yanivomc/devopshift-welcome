
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
  ami           = "ami-0c02fb55956c7d316" # Amazon Linux 2 AMI in us-east-1
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.sg.id]

  tags = {
    Name = "Yovel-vm"
  }
}

resource "time_sleep" "wait_for_ip" {
  create_duration = "5s"  # Introduce a delay of 30 seconds
}

resource "null_resource" "run_script" {
  provisioner "local-exec" {
    command = "echo 'i just run terraform apply.'"
  }
}

# resource "null_resource" "check_public_ip" {
#   provisioner "local-exec" {
#     command = <<EOT
#       if [ -z "${aws_instance.vm.public_ip}" ]; then
#         echo "ERROR: Public IP address was not assigned." >&2
#         exit 1
#       fi
#     EOT
#   }

#   depends_on = [aws_instance.vm]
# }

