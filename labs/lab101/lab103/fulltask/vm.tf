resource "aws_instance" "vm" {
 ami                         = data.aws_ami.terrformami.id
 instance_type               = var.vm_size
 vpc_security_group_ids      = [aws_security_group.sg.id]

 tags = {
   Name = var.vm_name
 }

 user_data = <<-EOF
   #cloud-config
   users:
     - name: ${var.admin_username}
       groups: sudo
       shell: /bin/bash
       sudo: ["ALL=(ALL) NOPASSWD:ALL"]
       lock_passwd: false
       passwd: $(echo ${var.admin_password} | openssl passwd -6 -stdin)
   EOF

 }

output "vm_public_ip" {
 value = aws_instance.vm.public_ip
}