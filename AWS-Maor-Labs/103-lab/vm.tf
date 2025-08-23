resource "aws_instance" "vm" {
 ami                         = var.ami
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


# -----------------------------------------------------------
# Notes regarding the user login configuration:
# 
# Explanation:
# 1. Cloud-Init:
#   - user_data allows you to pass initialization scripts to the EC2 instance during boot.
#   - The #cloud-config syntax is used to create users and set passwords.
#
# 2. Password Encryption:
#   - The `passwd` field requires a hashed password.
#   - Use `openssl passwd -6` to generate a secure hash for the password.
#   - Replace the hash generation dynamically if needed (e.g., in CI/CD pipelines).
#
# 3. Locking SSH:
#   - By not specifying an SSH key and relying on user_data, you enable user/password login.
#   - Ensure the AWS security group allows SSH (port 22) if required for initial configuration.
#
# 4. Security Considerations (TBD):
#   - Avoid hardcoding sensitive credentials in your Terraform code.
#   - Use secure methods to pass secrets, such as:
#     - Terraform variables stored in encrypted state files
#     - A secrets management solution (e.g., AWS Secrets Manager)
# -----------------------------------------------------------
