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
