
provider "aws" {
  region = "us-east-2"
}

variable "vpc_id" {
  default = "vpc-0a691b1cda1dea4be"
}

variable "subnet_ids" {
  default = ["subnet-09a9b4fe4e74051b3", "subnet-05860172a9327d826"]
}

resource "aws_instance" "web_server" {
  ami                    = "ami-0c995fbcf99222492"
  instance_type          = "t3.small"
  availability_zone      = "us-east-2"
  subnet_id              = var.subnet_ids[0]
  vpc_security_group_ids = [aws_security_group.lb_sg.id]

  tags = {
    Name = "WebServer"
  }
}

resource "aws_security_group" "lb_sg" {
  name        = "lb_security_group_Maor-lb"
  description = "Allow HTTP inbound traffic"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_lb" "application_lb" {
  name               = "Maor-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.lb_sg.id]
  subnets            = var.subnet_ids
}

resource "aws_lb_listener" "http_listener" {
  load_balancer_arn = aws_lb.application_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.web_target_group.arn
  }
}

resource "aws_lb_target_group" "web_target_group" {
  name     = "web-target-group-Maor-lb"
  port     = 80
  protocol = "HTTP"
  vpc_id   = var.vpc_id
}

resource "aws_lb_target_group_attachment" "web_instance_attachment" {
  target_group_arn = aws_lb_target_group.web_target_group.arn
  target_id        = aws_instance.web_server.id
}


output "instance_id" {
  value = aws_instance.web_server.id
}

output "load_balancer_dns" {
  value = aws_lb.application_lb.dns_name
}