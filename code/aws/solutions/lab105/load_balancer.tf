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