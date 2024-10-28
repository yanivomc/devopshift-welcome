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
