output "vm_public_ip" {
  value = azurerm_public_ip.pip-Maor.ip_address
  depends_on  = [time_sleep.wait_for_ip]  # Wait for the time_sleep resource to complete
  description = "Public IP address of the VM"
}
