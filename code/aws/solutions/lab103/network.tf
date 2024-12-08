


# Network Security Group
resource "azurerm_network_security_group" "nsg" {
  name                = "nsg-${var.yourname}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

# Public IP for the VM
resource "azurerm_public_ip" "pip" {
  name                = "pip-${var.yourname}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  allocation_method   = "Dynamic"
  sku                 = "Basic"
}

# Network Interface for the VM
resource "azurerm_network_interface" "nic" {
  name                = "nic-${var.yourname}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name                          = "internal-${var.yourname}"
    subnet_id                     = azurerm_subnet.subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.pip.id
  }
}

# Virtual Network for the subnet
resource "azurerm_virtual_network" "vnet" {
  name                = "vnet-${var.yourname}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  address_space       = ["10.0.0.0/16"]
}

# Subnet within the Virtual Network
resource "azurerm_subnet" "subnet" {
  name                 = "subnet-${var.yourname}"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}



