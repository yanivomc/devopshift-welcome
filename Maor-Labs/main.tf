provider "azurerm" {
  features {}
}



resource "azurerm_resource_group" "rg-Maor" {
  name = "Maor-resources"
  location = var.location
}


resource "azurerm_virtual_network" "vnet-Maor" {
  name                = "Maor-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = var.location
  resource_group_name = azurerm_resource_group.rg-Maor.name

}


resource "azurerm_subnet" "subnet-Maor" {
  name                 = "Maor-subnet"
  resource_group_name  = azurerm_resource_group.rg-Maor.name
  virtual_network_name = azurerm_virtual_network.vnet-Maor.name
  address_prefixes     = ["10.0.1.0/24"]
}



module "Maor_VM_1" {
    source = "./modules/vm"
    name = "Maor_VM_1"
    location = azurerm_resource_group.rg-Maor.location
    resource_group_name = azurerm_resource_group.rg-Maor.name
    subnet_id           = azurerm_subnet.subnet-Maor.id
    admin_username      = "testadmin"
    admin_password      = "Password1234!"   # In real use, move to secrets!
    vm_size = "Standard_B1ms"
}








