provider "azurerm" {
  features {}
}

variable "location" {
  default = "East US"
}

resource "azurerm_resource_group" "rg" {
  name     = "[YOURNAME]-resources"
  location = var.location
}


resource "azurerm_subnet" "subnet" {
  name                 = "[YOURNAME]-subnet"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}


resource "azurerm_virtual_network" "vnet" {
  name                = "[YOURNAME]-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_public_ip" "pip" {
  name                = "[YOURNAME]-pip"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
  allocation_method   = "Dynamic"  # Dynamic IP allocation for Basic SKU
  sku = "Basic"  # Use Basic SKU (Stock Keeping Unit - azure tiers) for dynamic IP
}

resource "azurerm_network_interface" "nic" {
  name                = "[YOURNAME]-nic"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name                          = "[YOURNAME]-ipconfig"
    subnet_id                     = azurerm_subnet.subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.pip.id
  }
}


variable "vm_size" {
  default = "Standard_B1ms"
}

variable "admin_username" {
  default = "adminuser"
}

variable "admin_password" {
  default = "Password123!"
}


resource "azurerm_linux_virtual_machine" "vm" {
  name                  = "[YOURNAME]-vm"
  location              = var.location
  resource_group_name   = azurerm_resource_group.rg.name
  network_interface_ids = [azurerm_network_interface.nic.id]
  size                  = var.vm_size

  os_disk {
    name              = "[YOURNAME]-os-disk"
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

  computer_name = "[YOURNAME]-vm"
}


output "vm_public_ip" {
  value = azurerm_public_ip.pip.ip_address
  description = "Public IP address of the VM"
}
