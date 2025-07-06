provider "azurerm" {
  features {}
}

variable "yourname" {
  default     = "Maor"
  description = "Change it to your first name and the first letter of your family name: ex. yanivc - for yaniv cohen"
}

variable "location" {
  default = "East US"
}