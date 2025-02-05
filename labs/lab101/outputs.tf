
output "vm_public_ip" {
  value       = aws_instance.vm.public_ip
  depends_on = [null_resource.check_public_ip] 
  #depends_on  = [time_sleep.wait_for_ip]  # Wait for the time_sleep resource to complete
  description = "Public IP address of the VM"
}
