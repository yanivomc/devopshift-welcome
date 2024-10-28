
# Mock the number of virtual machines needed
output "vm_count" {
  value = var.high_availability ? 3 : 1
  description = "Number of VMs required for the environment. If high availability is true, 3 VMs are needed; otherwise, 1."
}

# Mocking network requirements based on environment
output "network_configuration" {
  value = var.environment == "prod" ? "Production Network - Full Scale" : "Development/Staging Network - Limited Scale"
  description = "Provides the network configuration type based on the environment."
}

# Example of conditional logic using a ternary operator
output "ha_status_message" {
  value = var.high_availability ? "High availability is enabled - multiple VMs are needed." : "High availability is disabled - a single VM is sufficient."
  description = "A message indicating if high availability is enabled or disabled."
}

# Mocking subnet creation using for_each
locals {
  subnets = var.high_availability ? ["subnet-a", "subnet-b", "subnet-c"] : ["subnet-a"]
}

output "mock_subnet_list" {
  value = [for subnet in local.subnets : "Configured ${subnet}"]
  description = "A mocked list of subnets that would be created based on high availability."
}

