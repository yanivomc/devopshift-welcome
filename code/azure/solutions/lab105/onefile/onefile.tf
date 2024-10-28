# Define the provider and global variables
provider "azurerm" {
  features {}
}

variable "yourname" {
  default     = "yanivc"
  description = "Change it to your first name and the first letter of your family name: ex. yanivc - for yaniv cohen"
}

variable "vm_name" {
  default     = "vm-yanivc"
  description = "Change it to your first name and the first letter of your family name: ex. yanivc - for yaniv cohen"
}

variable "admin_username" {
  default     = "adminuser"
  description = "Username for the admin user on the VM"
}

variable "admin_password" {
  default     = "Password123!"
  description = "Password for the admin user on the VM"
}

variable "location" {
  default     = "East US"
  description = "Azure region where resources will be deployed"
}

variable "vm_size" {
  default     = "Standard_B1ms"
  description = "Size of the virtual machine"
}

# Resource Group
resource "azurerm_resource_group" "rg" {
  name     = "rg-${var.yourname}"
  location = var.location
}

# Load Balancer Public IP (Shared IP)
resource "azurerm_public_ip" "lb_pip" {
  name                = "lb-pip-${var.yourname}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  allocation_method   = "Static"
  sku                 = "Standard"
}

# Load Balancer
resource "azurerm_lb" "lb" {
  name                = "lb-${var.yourname}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Standard"

  frontend_ip_configuration {
    name                 = "LoadBalancerFrontEnd"
    public_ip_address_id = azurerm_public_ip.lb_pip.id
  }
}

# Backend Address Pool for Load Balancer
resource "azurerm_lb_backend_address_pool" "lb_pool" {
  loadbalancer_id = azurerm_lb.lb.id
  name            = "backend-pool-${var.yourname}"
}

# Load Balancer Probe to check VM health
resource "azurerm_lb_probe" "lb_probe" {
  loadbalancer_id     = azurerm_lb.lb.id
  name                = "http-probe-${var.yourname}"
  protocol            = "Http"
  port                = 80
  request_path        = "/welcome.html"
  interval_in_seconds = 15
  number_of_probes    = 3
}

# Load Balancer Rule to Distribute Traffic
resource "azurerm_lb_rule" "lb_rule" {
  loadbalancer_id                = azurerm_lb.lb.id
  name                           = "http-rule-${var.yourname}"
  protocol                       = "Tcp"
  frontend_port                  = 80
  backend_port                   = 80
  frontend_ip_configuration_name = "LoadBalancerFrontEnd"
  backend_address_pool_ids       = [azurerm_lb_backend_address_pool.lb_pool.id]
  probe_id                       = azurerm_lb_probe.lb_probe.id
}

# Network Security Group
resource "azurerm_network_security_group" "nsg" {
  name                = "nsg-${var.yourname}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

# Network Security Rule to Allow SSH and HTTP
resource "azurerm_network_security_rule" "allow_http_ssh" {
  name                        = "allow-http-ssh-${var.vm_name}"
  priority                    = 100
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_ranges     = ["80", "22"]
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  resource_group_name         = azurerm_resource_group.rg.name
  network_security_group_name = azurerm_network_security_group.nsg.name
}

# Public IP for the VMs
resource "azurerm_public_ip" "vm_pip" {
  count               = 2
  name                = "pip-${var.yourname}-${count.index + 1}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  allocation_method   = "Static"
  sku                 = "Standard"
}

# Network Interface for the VMs
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

# Associate Network Interface with Load Balancer Backend Pool
resource "azurerm_network_interface_backend_address_pool_association" "nic_lb_pool_association" {
  count                    = 2
  network_interface_id     = azurerm_network_interface.nic[count.index].id
  ip_configuration_name    = "internal-${var.yourname}-${count.index + 1}"
  backend_address_pool_id  = azurerm_lb_backend_address_pool.lb_pool.id
}

# Associate NSG with Network Interfaces
resource "azurerm_network_interface_security_group_association" "nic_nsg_association" {
  count                    = 2
  network_interface_id     = azurerm_network_interface.nic[count.index].id
  network_security_group_id = azurerm_network_security_group.nsg.id
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

# Linux Virtual Machine configuration to create multiple VMs
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

# Null Resource for Apache Installation
resource "null_resource" "provision_apache" {
  count      = 2
  depends_on = [azurerm_linux_virtual_machine.vm]

  # Trigger to force rerun whenever timestamp changes
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

# Output for Load Balancer Public IP
output "load_balancer_ip" {
  value       = azurerm_public_ip.lb_pip.ip_address
  description = "The public IP address of the load balancer."
}

# Output the Server Information for Each VM
output "server_info" {
  value = [
    for i in range(2) : "Please browse: http://${azurerm_public_ip.lb_pip.ip_address}/welcome.html. Server: ${azurerm_linux_virtual_machine.vm[i].computer_name}"
  ]
  description = "Instructions to access the web server through the load balancer."
}
