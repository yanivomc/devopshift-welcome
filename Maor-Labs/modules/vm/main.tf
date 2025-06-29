

resource "azurerm_public_ip" "pip-Maor" {
  name                = "Maor-pip"
  location            = var.location
  resource_group_name = var.name
  allocation_method   = "Dynamic"  # Dynamic IP allocation for Basic SKU
  sku = "Basic"  
}

resource "azurerm_network_interface" "nic-Maor" {
  name                = "Maor-nic"
  location            = var.location
  resource_group_name = var.name

  ip_configuration {
    name                          = "Maor-ipconfig"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "azurerm_public_ip.pip-Maor"
  }
}


resource "azurerm_linux_virtual_machine" "vm-Maor" {
  name                  = "Maor-vm"
  location              = var.location
  resource_group_name   = var.name
  network_interface_ids = [azurerm_network_interface.nic-Maor.id]
  size                  = var.vm_size

  os_disk {
    name              = "Maor-os-disk"
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  admin_username = var.admin_username
  admin_password = var.admin_password

  disable_password_authentication = false

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  computer_name = "Maor-vm"
}


resource "time_sleep" "wait_for_ip" {
  create_duration = "30s"  # Wait for 30 seconds
}

