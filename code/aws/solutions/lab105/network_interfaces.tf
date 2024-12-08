resource "azurerm_public_ip" "vm_pip" {
  count               = 2
  name                = "pip-${var.yourname}-${count.index + 1}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  allocation_method   = "Static"
  sku                 = "Standard"
}

resource "azurerm_network_interface" "nic" {
  count               = 2
  name                = "nic-${var.yourname}-${count.index + 1}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name                          = "internal-${var.yourname}-${count.index + 1}"
    subnet_id                     = azurerm_subnet.subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.vm_pip[count.index].id
  }
}

# Adding both nic's into our LB Pool
resource "azurerm_network_interface_backend_address_pool_association" "nic_lb_pool_association" {
  count                    = 2
  network_interface_id     = azurerm_network_interface.nic[count.index].id
  ip_configuration_name    = "internal-${var.yourname}-${count.index + 1}"
  backend_address_pool_id  = azurerm_lb_backend_address_pool.lb_pool.id
}

# Adding both Nic's to the NSG
resource "azurerm_network_interface_security_group_association" "nic_nsg_association" {
  count                    = 2
  network_interface_id     = azurerm_network_interface.nic[count.index].id
  network_security_group_id = azurerm_network_security_group.nsg.id
}
