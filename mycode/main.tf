terraform {
  required_providers {
    time = {
      source = "hashicorp/time"
      version = "0.7.2"  # Ensure you're using the latest version
    }
  }
}

provider "azurerm" {
  features {}
}

variable "location" {
  default = "East US"
}

resource "azurerm_resource_group" "rg-yaniv" {
  name     = "yaniv-resources"
  location = var.location
}

resource "azurerm_virtual_network" "vnet-yaniv" {
  name                = "yaniv-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = var.location
  resource_group_name = azurerm_resource_group.rg-yaniv.name
}

resource "azurerm_subnet" "subnet-yaniv" {
  name                 = "yaniv-subnet"
  resource_group_name  = azurerm_resource_group.rg-yaniv.name
  virtual_network_name = azurerm_virtual_network.vnet-yaniv.name
  address_prefixes     = ["10.0.1.0/24"]
}



resource "azurerm_public_ip" "pip-yaniv" {
  name                = "yaniv-pip"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg-yaniv.name
  allocation_method   = "Dynamic"  
  sku = "Basic"  
}

resource "azurerm_network_interface" "nic-yaniv" {
  name                = "yaniv-nic"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg-yaniv.name

  ip_configuration {
    name                          = "yaniv-ipconfig"
    subnet_id                     = azurerm_subnet.subnet-yaniv.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.pip-yaniv.id
  }
}


variable "vm_size" {
  default = "Standard_B1ms"
}

variable "admin_username" {
  default = "adminuser-yaniv"
}

variable "admin_password" {
  default = "Password123!"
}


resource "azurerm_linux_virtual_machine" "vm-yaniv" {
  name                  = "yaniv-vm"
  location              = var.location
  resource_group_name   = azurerm_resource_group.rg-yaniv.name
  network_interface_ids = [azurerm_network_interface.nic-yaniv.id]
  size                  = var.vm_size

  os_disk {
    name              = "yaniv-os-disk"
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

  computer_name = "yaniv-vm"
}

resource "time_sleep" "wait_for_ip" {
  create_duration = "30s"  # Wait for 30 seconds
}


output "vm_public_ip" {
  value = azurerm_public_ip.pip-yaniv.ip_address
  description = "Public IP address of the VM"
  depends_on = [time_sleep.wait_for_ip]
}

