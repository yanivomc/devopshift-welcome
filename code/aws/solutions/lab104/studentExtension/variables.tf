# Variable to control environment type
variable "environment" {
  description = "Define the environment type: dev, staging, or prod"
  type        = string
  default     = "dev"
}

# Variable to control high availability
variable "high_availability" {
  description = "Whether to enable high availability (true or false)"
  type        = bool
  default     = false
}

# Variable to control mock database creation
variable "create_database" {
  description = "Whether to create a mock database (true or false)"
  type        = bool
  default     = false
}