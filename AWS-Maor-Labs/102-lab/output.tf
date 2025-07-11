#   To retrieve the public IP of the virtual machine, use the following output configuration:
output "vm_public_ip" {
  value       = aws_instance.vm.public_ip
  description = "Public IP address of the VM"
}

