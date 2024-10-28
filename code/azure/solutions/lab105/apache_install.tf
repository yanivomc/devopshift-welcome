resource "null_resource" "provision_apache" {
  count      = 2
  depends_on = [azurerm_linux_virtual_machine.vm]

  triggers = {
    always_run = timestamp()
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install -y apache2",
      "echo '<h1>Welcome to \"${azurerm_linux_virtual_machine.vm[count.index].computer_name}\" Web Server!</h1>' | sudo tee /var/www/html/welcome.html",
      "sudo systemctl start apache2",
      "sudo systemctl enable apache2"
    ]

    connection {
      type     = "ssh"
      user     = var.admin_username
      password = var.admin_password
      host     = azurerm_public_ip.vm_pip[count.index].ip_address
      timeout  = "1m"
    }
  }
}
