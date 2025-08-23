variable "environment" {
  description = "Define the environment type: dev, staging, or prod"
  type        = string
  default     = "prod" # dev
}

variable "high_availability" {
  description = "Whether to enable high availability (true or false)"
  type        = bool
  default     = true # false
}

variable "create_database" {
    description = "This should be a boolean (true or false) that decides if a mock database should be created"
    type = bool
    default = true # false
}

