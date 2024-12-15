# VARIABLES
variable "instance_count" {
  description = "Number of EC2 instances to create"
  default     = 2
}

variable "region" {
  default     = "us-west-2"
  description = "AWS Region"
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
# *********

# PROVIDER
provider "aws" {
  region = var.region
}

# SECURITY GROUP FOR ALB
resource "aws_security_group" "alb_sg" {
  name        = "alb-sg"
  description = "Security group for ALB"

  vpc_id = data.aws_vpc.default.id

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

  tags = {
    Name = "alb-sg"
  }
}

# SECURITY GROUP FOR EC2
resource "aws_security_group" "ec2_sg" {
  name        = "ec2-sg"
  description = "Security group for EC2 instances"

  vpc_id = data.aws_vpc.default.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

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

  tags = {
    Name = "ec2-sg"
  }
}

# DATA SOURCE: DEFAULT VPC AND SUBNETS
data "aws_vpc" "default" {
  default = true
}

data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

# TARGET GROUP
resource "aws_lb_target_group" "tg" {
  name     = "alb-target-group"
  port     = 80
  protocol = "HTTP"
  vpc_id   = data.aws_vpc.default.id

  health_check {
    enabled             = true
    interval            = 30
    path                = "/"
    port                = "traffic-port"
    protocol            = "HTTP"
    healthy_threshold   = 3
    unhealthy_threshold = 2
    timeout             = 5
  }

  tags = {
    Name = "alb-tg"
  }
}


# Null Resource for Apache Installation
resource "null_resource" "provision_apache" {
  count         = var.instance_count
  depends_on = [aws_instance.ec2]

  # Trigger to force rerun whenever timestamp changes
  # This will force terraform to rerun the provisioner and update the welcome.html file if changed
  triggers = {
    always_run = timestamp()
  }

  provisioner "remote-exec" {
    inline = [
      # Check if update is already done
      "[ -f /tmp/update_done ] && echo 'Update already completed. Skipping...' || (echo 'Running update for the first time...' && sudo apt update && touch /tmp/update_done)",
      # check if apache is installed or not
      "if ! pidof apache2 > /dev/null; then sudo apt install -y apache2; fi" ,
      # Create / update the welcome.html file
      "echo '<h1>Welcome to the Web Server ${aws_instance.ec2[count.index].tags.Name}!</h1>' | sudo tee /var/www/html/welcome.html",
      "sudo systemctl start apache2",
      "sudo systemctl enable apache2"
    ]

    connection {
      type     = "ssh"
      user     = "ubuntu"
      password = var.admin_password
      host     = aws_instance.ec2[count.index].public_ip
      timeout  = "1m"
    }
  }
}



# EC2 INSTANCES
resource "aws_instance" "ec2" {
  count         = var.instance_count
  ami           = var.ami
  instance_type = var.vm_size
  subnet_id     = data.aws_subnets.default.ids[count.index % length(data.aws_subnets.default.ids)]
  vpc_security_group_ids = [aws_security_group.ec2_sg.id]

  tags = {
    Name = "ec2-instance-${count.index}"
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

# REGISTER EC2 INSTANCES TO TARGET GROUP
resource "aws_lb_target_group_attachment" "tg_attachment" {
  for_each = { for idx, instance in aws_instance.ec2 : idx => instance }

  target_group_arn = aws_lb_target_group.tg.arn
  target_id        = each.value.id
  port             = 80
}

# APPLICATION LOAD BALANCER
resource "aws_lb" "alb" {
  name               = "app-load-balancer"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb_sg.id]
  subnets            = data.aws_subnets.default.ids

  enable_deletion_protection = false

  tags = {
    Name = "application-lb"
  }
}

# LISTENER
resource "aws_lb_listener" "http_listener" {
  load_balancer_arn = aws_lb.alb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.tg.arn
  }
}






# NULL RESOURCE TO CHECK TARGET HEALTH
resource "null_resource" "validate_lb_targets" {
  
  provisioner "local-exec" {
    command = <<EOT
      echo "*** VALIDATING TARGET HEALTH ***"
      echo "Target Group ARN: ${aws_lb_target_group.tg.arn}"
      echo "Checking Load Balancer Target Group Health..."

      retry_check=5 # number of retries to check target health
      unhealthy_count=0 

      while [ $retry_check -gt 0 ]; do
        aws elbv2 describe-target-health \
          --region="${var.region}" \
          --target-group-arn "${aws_lb_target_group.tg.arn}" \
          --query 'TargetHealthDescriptions[*].[Target.Id,TargetHealth.State]' \
          --output text > target_health.txt

        while read target_id status; do
          echo "Target ID: $target_id - Status: $status"
          if [ "$status" != "healthy" ]; then
            echo "Unhealthy Target: $target_id"
            unhealthy_count=$((unhealthy_count + 1))
          fi
        done < target_health.txt

        if [ $unhealthy_count -gt 0 ]; then
          echo "Some targets are unhealthy. Check target_health.txt for details."
          echo "Retrying in 30 seconds..."
          sleep 10
          retry_check=$((retry_check - 1))
          unhealthy_count=0
        else
          echo "All targets are healthy."
          break
        fi
      done
    EOT
  }

  triggers = {
    always_run = timestamp()
  }

  # depends_on = [aws_lb_target_group_attachment.tg_attachment]
  depends_on = [ null_resource.provision_apache ]
}

# OUTPUTS
# OUTPUT: ALB DNS NAME
output "alb_dns_name" {
  value       = "Please allow couple of mintues for DNS propogation on first run before you  browse: http://${aws_lb.alb.dns_name}/welcome.html"
  description = "DNS Name of the Load Balancer"
}

output "per_server_info" {
  value = [
    for idx, instance in aws_instance.ec2 : 
    "Please browse: http://${instance.public_ip}/welcome.html. Server: ${instance.tags.Name}"
  ]
  description = "Instructions to access the web server through the load balancer."
}


# OUTPUT: INSTRUCTIONS FOR VALIDATION
output "validation_message" {
  value       = "Run terraform apply to validate the health of ALB targets using AWS CLI. Check the console output."
  description = "Instructions for validating target health."
}
