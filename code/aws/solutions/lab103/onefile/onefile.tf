provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-west-2"
}


variable "ami" {
  default = "ami-04feae287ec8b0244"
  
}
variable "vm_name" {
  default = "vm-[YOURNAME]"
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


resource "aws_security_group" "sg" {
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
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

resource "time_sleep" "wait_for_ip" {
  create_duration = "1m"  # Wait for 1 minute to allow AWS to allocate the IP
}

resource "null_resource" "validate_ip" {
  provisioner "local-exec" {
    command = <<EOT
      retries=4
      interval=30
      for i in $(seq 1 $retries); do
        if [ -z "${aws_instance.vm.public_ip}" ]; then
          echo "Attempt $i: Public IP address not assigned yet, retrying in $interval seconds..."
          sleep $interval
        else
          echo "Public IP address assigned: ${aws_instance.vm.public_ip}"
          exit 0
        fi
      done
      echo "ERROR: Public IP address was not assigned after $retries attempts." >&2
      exit 1
    EOT
  }
  depends_on = [time_sleep.wait_for_ip]
}

resource "aws_instance" "vm" {
  ami                         = var.ami
  instance_type               = var.vm_size
  vpc_security_group_ids      = [aws_security_group.sg.id]

  tags = {
    Name = var.vm_name
  }

  user_data = <<-EOF
    #cloud-config
    users:
      - name: ${var.admin_username}
        groups: sudo
        shell: /bin/bash
        sudo: ["ALL=(ALL) NOPASSWD:ALL"]
        lock_passwd: false
        passwd: $(echo ${var.admin_password} | openssl passwd -6 -stdin)
    EOF

  
}

output "vm_public_ip" {
  value = aws_instance.vm.public_ip
}


# Null Resource for Apache Installation
resource "null_resource" "provision_apache" {
  depends_on = [aws_instance.vm]

  # Trigger to force rerun whenever timestamp changes
  # This will force terraform to rerun the provisioner and update the welcome.html file if changed
  triggers = {
    always_run = timestamp()
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install -y apache2",
      "echo '<h1>Welcome to the Web Server!</h1>' | sudo tee /var/www/html/welcome.html",
      "sudo systemctl start apache2",
      "sudo systemctl enable apache2"
    ]

    connection {
      type     = "ssh"
      user     = "ubuntu"
      password = var.admin_password
      host     = aws_instance.vm.public_ip
      timeout  = "1m"
    }
  }
}


# Updated Output for Server Information to use data source
output "server_info" {
  value       = "Please browse: http://${aws_instance.vm.public_ip}/welcome.html"
  description = "Instructions to access the server, noting that port 80 is currently blocked."
}