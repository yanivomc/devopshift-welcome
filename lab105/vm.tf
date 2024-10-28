resource "azurerm_linux_virtual_machine" "vm" {
  count                 = 2
  name                  = "${var.vm_name}-${count.index + 1}"
  location              = var.location
  resource_group_name   = azurerm_resource_group.rg.name
  network_interface_ids = [azurerm_network_interface.nic[count.index].id]
  size                  = var.vm_size

  os_disk {
    name                 = "os-disk-${var.yourname}-${count.index + 1}"
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  admin_username = var.admin_username
  admin_password = var.admin_password

  disable_password_authentication = false
  computer_name                   = "${var.vm_name}-${count.index + 1}"

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  lifecycle {
    ignore_changes = [network_interface_ids]
  }

  depends_on = [azurerm_network_interface.nic, azurerm_public_ip.lb_pip]
}