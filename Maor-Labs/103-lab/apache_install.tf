
# Null Resource for Apache Installation
resource "null_resource" "provision_apache" {
  depends_on = [azurerm_linux_virtual_machine.vm]

  # Trigger to force rerun whenever timestamp changes
  triggers = {
    always_run = timestamp()
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install -y apache2",
      "echo '<h1>Welcome to \"${azurerm_linux_virtual_machine.vm.computer_name}\" Web Server!</h1>' | sudo tee /var/www/html/welcome.html",
      "sudo systemctl start apache2",
      "sudo systemctl enable apache2"
    ]

    connection {
      type     = "ssh"
      user     = var.admin_username
      password = var.admin_password
      host     = data.azurerm_public_ip.example.ip_address
      timeout  = "1m"
    }
  }
}

# Updated Output for Server Information to use data source
output "server_info" {
  value       = "Please browse: http://${data.azurerm_public_ip.example.ip_address}/welcome.html"
  description = "Browse the above link"
}

