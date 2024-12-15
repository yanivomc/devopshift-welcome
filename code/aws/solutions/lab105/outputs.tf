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
