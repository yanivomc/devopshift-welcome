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



terraform_template = """
#########################
#  Terraform Template   #
#########################

provider "aws" {
  region = "{{ region }}"
}

#####################
#  Existing Network #
#####################
# משתמשים ב-IDs שמועברים מה-context
# vpc_id           = {{ vpc_id }}
# subnet_id_1/2    = {{ subnet_id_1 }} , {{ subnet_id_2 }}
# security_group   = {{ security_group_id }}

#####################
#  EC2 Web Server   #
#####################
resource "aws_instance" "web_server" {
  ami                    = "{{ ami }}"
  instance_type          = "{{ instance_type }}"
  subnet_id              = "{{ subnet_id_1 }}"
  vpc_security_group_ids = ["{{ security_group_id }}"]

  user_data = <<-EOF
    #!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "<h1>Hello from $(hostname -f)</h1>" > /var/www/html/index.html
  EOF

  tags = {
    Name = "WebServer"
  }
}

#################################
#  Application Load Balancer    #
#################################
resource "aws_lb" "application_lb" {
  name               = "{{ load_balancer_name | lower }}"
  internal           = false
  load_balancer_type = "application"
  security_groups    = ["{{ security_group_id }}"]
  subnets            = ["{{ subnet_id_1 }}", "{{ subnet_id_2 }}"]

  enable_deletion_protection = false

  tags = {
    Name = "{{ load_balancer_name | lower }}"
  }
}

##################
#  Target Group  #
##################
resource "aws_lb_target_group" "web_target_group" {
  name     = "{{ load_balancer_name | lower }}-tg"
  port     = 80
  protocol = "HTTP"
  vpc_id   = "{{ vpc_id }}"

  health_check {
    enabled             = true
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 5
    interval            = 30
    path                = "/"
    matcher             = "200"
  }
}

##############################
#  Attach EC2 → TargetGroup  #
##############################
resource "aws_lb_target_group_attachment" "web_instance_attachment" {
  target_group_arn = aws_lb_target_group.web_target_group.arn
  target_id        = aws_instance.web_server.id
  port             = 80
}

#################
#  LB Listener  #
#################
resource "aws_lb_listener" "http_listener" {
  load_balancer_arn = aws_lb.application_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.web_target_group.arn
  }
}

############
# Outputs  #
############
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.web_server.id
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.web_server.public_ip
}

output "load_balancer_dns" {
  description = "DNS name of the load balancer"
  value       = aws_lb.application_lb.dns_name
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
        "load_balancer_name": context["lb_name"] ,
        "security_group_id": "sg-0123456789abcdef0",  # ← SG קיים
        "subnet_id_1": "subnet-09a9b4fe4e74051b3",    # AZ: us-east-2a
        "subnet_id_2": "subnet-0fa3e3e7dad301962",    # AZ: us-east-2b
        "vpc_id": "vpc-0a691b1cda1dea4be"             # VPC קיים
    }

    # print(template_context)

    template = jinja2.Template(terraform_template)
    
    rendered = template.render(template_context)

    return rendered