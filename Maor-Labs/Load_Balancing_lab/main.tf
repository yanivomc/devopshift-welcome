
resource "azurerm_resource_group" "rg-Maor" {
  name = "${var.yourname}-resources"
  location = var.location
}


# Provides a public IP address for the Load Balancer, allowing clients from the internet to access the resources behind it.
resource "azurerm_public_ip" "lb_pip" {
  name                = "lb-pip-${var.yourname}"                           # The name of the public IP resource, uniquely generated using the user's name.
  location            = azurerm_resource_group.rg-Maor.location      # location and resource_group_name: The location and resource group where the public IP is deployed, ensuring consistency with other resources.
  resource_group_name = azurerm_resource_group.rg-Maor.name          
  allocation_method   = "Static"                                # allocation_method: Set to Static, meaning the IP will remain constant, which is useful for reliable access.
  sku                 = "Standard"                              # Set to Standard, which is necessary to work with a Standard Load Balancer.
}


#  Creates the actual Load Balancer, which distributes incoming traffic among multiple virtual machines (VMs).
resource "azurerm_lb" "lb" {
  name                = "lb-${var.yourname}"
  location            = azurerm_resource_group.rg-Maor.location
  resource_group_name = azurerm_resource_group.rg-Maor.name
  sku                 = "Standard"

    # Defines the entry point for incoming traffic.
  frontend_ip_configuration {
    name                 = "LoadBalancerFrontEnd"
    public_ip_address_id = azurerm_public_ip.lb_pip.id
  }
}

#  Defines the Backend Address Pool, which contains the VMs that will receive the traffic distributed by the load balancer.
resource "azurerm_lb_backend_address_pool" "lb_pool" {
  loadbalancer_id = azurerm_lb.lb.id                    # Associates the backend pool with the previously created Load Balancer.
  name            = "backend-pool-${var.yourname}"
}


#  A Health Probe is used to check the health of the VMs in the backend pool. It helps decide if a VM can handle traffic or should be temporarily removed from the pool.
resource "azurerm_lb_probe" "lb_probe" {
  loadbalancer_id     = azurerm_lb.lb.id                # Links the probe to the Load Balancer.
  name                = "http-probe-${var.yourname}"
  protocol            = "Http"
  port                = 80
  request_path        = "/welcome.html"
  interval_in_seconds = 15
  number_of_probes    = 3
}


#  Defines how incoming traffic is handled by the load balancer. The Load Balancer Rule determines how requests to a specific port are routed to the backend pool.
resource "azurerm_lb_rule" "lb_rule" {
  loadbalancer_id                = azurerm_lb.lb.id
  name                           = "http-rule-${var.yourname}"
  protocol                       = "Tcp"
  frontend_port                  = 80
  backend_port                   = 80
  frontend_ip_configuration_name = "LoadBalancerFrontEnd"                           #  References the Frontend IP configuration created earlier.
  backend_address_pool_ids       = [azurerm_lb_backend_address_pool.lb_pool.id]     #  Points to the Backend Address Pool (azurerm_lb_backend_address_pool.lb_pool.id), defining which VMs will receive the incoming traffic.
  probe_id                       = azurerm_lb_probe.lb_probe.id                     # References the Health Probe to determine if a backend VM is healthy and can serve traffic.
}





