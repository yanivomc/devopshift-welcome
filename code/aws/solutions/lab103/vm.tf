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
      host     = self.public_ip
      timeout  = "1m"
    }
  }
}

output "vm_public_ip" {
  value = aws_instance.vm.public_ip
}

output "vm_http_url" {
  value = "http://${aws_instance.vm.public_ip}/welcome.html"
}
