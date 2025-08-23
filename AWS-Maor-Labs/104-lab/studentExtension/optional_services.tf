# Local variable to manage the list of services including cache if applicable
locals {
  # Adding "cache" to the list if `environment` is "prod" and `create_database` is true
  extended_services = var.environment == "prod" && var.create_database ? concat(local.services, ["cache"]) : local.services
}

# Output the extended list of services
output "extended_services_list" {
  value = [for service in local.extended_services : "Configured ${service} service"]
  description = "A mocked list of services that would be created, optionally including cache for production."
}