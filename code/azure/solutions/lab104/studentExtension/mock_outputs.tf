# Output to show how many VMs would be created
output "vm_count" {
  value = var.high_availability ? 3 : 1
  description = "Number of VMs required for the environment. If high availability is true, 3 VMs are needed; otherwise, 1."
}

# Output to show the environment network configuration
output "network_configuration" {
  value = var.environment == "prod" ? "Production Network - Full Scale" : "Development/Staging Network - Limited Scale"
  description = "Provides the network configuration type based on the environment."
}

# Output to indicate high availability status
output "ha_status_message" {
  value = var.high_availability ? "High availability is enabled - multiple VMs are needed." : "High availability is disabled - a single VM is sufficient."
  description = "A message indicating if high availability is enabled or disabled."
}

# Output to mock database creation
output "mock_database_creation" {
  value = var.create_database ? "A mock database will be created for this environment." : "No database needed for this environment."
  description = "Indicates whether a mock database should be created."
}
