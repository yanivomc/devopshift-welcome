
# Wait for IP Allocation
resource "time_sleep" "wait_for_ip" {
  create_duration = "1.5m"  # Wait for 1.5 minute to allow Azure to allocate the IP
}

# Null Resource to Validate IP Allocation
resource "null_resource" "validate_ip" {
  provisioner "local-exec" {
    command = <<EOT
      retries=4
      interval=15
      for i in $(seq 1 $retries); do
        if [ -z "${azurerm_public_ip.pip.ip_address}" ]; then
          echo "Attempt $i: Public IP address not assigned yet, retrying in $interval seconds..."
          sleep $interval
        else
          echo "Public IP address assigned: ${azurerm_public_ip.pip.ip_address}"
          exit 0
        fi
      done
      echo "ERROR: Public IP address was not assigned after $retries attempts." >&2
      exit 1
    EOT
  }
  depends_on = [time_sleep.wait_for_ip]
}

# Data Source to Reference Public IP after Validation
data "azurerm_public_ip" "example" {
  name                = azurerm_public_ip.pip.name
  resource_group_name = azurerm_resource_group.rg.name
  depends_on          = [null_resource.validate_ip]
}

