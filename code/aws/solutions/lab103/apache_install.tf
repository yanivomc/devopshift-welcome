resource "null_resource" "provision_apache" {
  depends_on = [aws_instance.vm]

  triggers = {
    always_run = timestamp()
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install -y apache2",
      "echo '<h1>Welcome to \"${aws_instance.vm.tags.Name}\" Web Server!</h1>' | sudo tee /var/www/html/welcome.html",
      "sudo systemctl start apache2",
      "sudo systemctl enable apache2"
    ]

    connection {
      type     = "ssh"
      user     = var.admin_username
      password = var.admin_password
      host     = aws_instance.vm.public_ip
      timeout  = "1m"
    }
  }
}

output "server_info" {
  value       = "Please browse: http://${aws_instance.vm.public_ip}/welcome.html"
  description = "Browse the above link"
}