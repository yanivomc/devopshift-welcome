variable "name" {
    description = "this is the name default"
    default = "Maor_VM"
    validation {
        condition     = contains(["Maor_VM_1", "Maor_VM_2"], var.name)
        error_message = "Environment must be either Maor_VM_1 or Maor_VM_2."
  }

}
variable "location" {
    description = "this is the location default"
    default = "West Europe"
}
variable "resource_group_name" {
    description = "this is the location default"
    default = "test"
}
variable "subnet_id" {}
variable "admin_username" {}
variable "admin_password" {}

variable "vm_size" {
  default = "Standard_B1ms"
}
