import jinja2

# Extract user inputs from the context dictionary
ami_options = {
    "ubuntu": "ami-0c995fbcf99222492",
    "amazon linux": "ami-0915e09cc7ceee3ab"
}

instance_types = {
    "t3.small": "t3.small",
    "t3.medium": "t3.medium"
}



AVAILABILITY_ZONES = ["us-east-2a", "us-east-2b"]
ALLOWED_REGION = "us-east-2"



terraform_template =  """
provider "aws" {
  region = "{{ region }}"
}

variable "vpc_id" {
  default = "vpc-0a691b1cda1dea4be"
}

variable "subnet_ids" {
  default = ["subnet-09a9b4fe4e74051b3", "subnet-05860172a9327d826"]
}

resource "aws_instance" "web_server" {
  ami                    = "{{ ami }}"
  instance_type          = "{{ instance_type }}"
  availability_zone      = "{{ availability_zone }}"
  subnet_id              = var.subnet_ids[0]
  vpc_security_group_ids = [aws_security_group.lb_sg.id]

  tags = {
    Name = "WebServer"
  }
}

resource "aws_security_group" "lb_sg" {
  name        = "lb_security_group_{{ load_balancer_name }}"
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
  name               = "{{ load_balancer_name }}"
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
  name     = "web-target-group-{{ load_balancer_name }}"
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
"""







def render_template(context):

    # print(context)

    ami_key = context["ami"].lower()
    ami_id = ami_options.get(ami_key)

    if not ami_id:
        sys.exit("❌ No valid AMI ID found for your choice.")


    ami_key = context["ami"].lower()
    ami_id = ami_options.get(ami_key)

    if not ami_id:
        raise ValueError(f"❌ Invalid AMI name '{ami_key}'. Must be one of: {list(ami_options.keys())}")

    # print(f"✅ AMI ID for '{ami_key}': {ami_id}")


    instance_type = instance_types.get(context["instance_type"].lower(), "t3.small")

    template_context = {
    "ami": ami_id,
    "instance_type": instance_type,
    "region": context["region"],
    "availability_zone": context["availability_zone"],
    "load_balancer_name": context["lb_name"]
    # Do NOT pass vpc_id or subnet_ids here, since they're defined as Terraform variables
}

    # print(template_context)

    template = jinja2.Template(terraform_template)
    
    rendered = template.render(template_context)

    return rendered