# Local variable to manage the list of services based on `create_database`
locals {
  services = var.create_database ? ["web", "api", "database"] : ["web", "api"]
}

# Output the mock list of services
output "mock_services_list" {
  value = [for service in local.services : "Configured ${service} service"]
  description = "A mocked list of services that would be created based on the create_database variable."
}