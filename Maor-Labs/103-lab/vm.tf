
# Linux Virtual Machine configuration
resource "azurerm_linux_virtual_machine" "vm" {
  name                  = var.vm_name
  location              = var.location
  resource_group_name   = azurerm_resource_group.rg.name
  network_interface_ids = [azurerm_network_interface.nic.id]
  size                  = var.vm_size

  os_disk {
    name                 = "os-disk-${var.yourname}"
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  admin_username = var.admin_username
  admin_password = var.admin_password

  disable_password_authentication = false
  computer_name                   = var.vm_name

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  # Ignore changes to the network interface to avoid unnecessary recreation of the VM
  lifecycle {
    ignore_changes = [network_interface_ids]
  }

  depends_on = [azurerm_network_interface.nic, azurerm_public_ip.pip]
}

