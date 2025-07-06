
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

output "Mock_Database_Output" {
    description = "Use an output block to print a message based on the create_database variable"
    value = var.create_database ? "A mock database will be created for this environment." : "No database needed for this environment."
}

locals {
  database_value = var.create_database ? ["web", "api", "database"] : ["web", "api"]
}

output "Add_Another_Output_Using_For_each" {
    description = "Use for_each to create a list of mock services based on the create_database value"
    value = [ for db_value in local.database_value : "Value: ${db_value}"]
}