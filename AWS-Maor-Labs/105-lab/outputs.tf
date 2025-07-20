# outputs.tf
output "ec2_instance_id" {
  value = aws_instance.web_server.id
}

output "ec2_public_ip" {
  value = aws_instance.web_server.public_ip
}

output "vpc_id" {
  value = module.vpc.public_subnet_id
  # value = aws_vpc.lab_vpc.id
}
