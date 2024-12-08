resource "aws_instance" "vm" {
  ami                         = "ami-0c02fb55956c7d316"
  instance_type               = var.vm_size
  vpc_security_group_ids      = [aws_security_group.sg.id]

  tags = {
    Name = var.vm_name
  }

  # ec2 does not allow password login by default - threfore we need to create a new user and password using cloud-init
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

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install -y apache2",
      "echo '<h1>Welcome to the Web Server!</h1>' | sudo tee /var/www/html/welcome.html",
      "sudo systemctl start apache2",
      "sudo systemctl enable apache2"
    ]
  }
}

output "vm_public_ip" {
  value       = aws_instance.vm.public_ip
}

output "vm_http_url" {
  value       = "http://${aws_instance.vm.public_ip}/welcome.html"
}