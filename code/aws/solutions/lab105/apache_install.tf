# Null Resource for Apache Installation
resource "null_resource" "provision_apache" {
  count         = var.instance_count
  depends_on = [aws_instance.ec2]

  # Trigger to force rerun whenever timestamp changes
  # This will force terraform to rerun the provisioner and update the welcome.html file if changed
  triggers = {
    always_run = timestamp()
  }

  provisioner "remote-exec" {
    inline = [
      # Check if update is already done
      "[ -f /tmp/update_done ] && echo 'Update already completed. Skipping...' || (echo 'Running update for the first time...' && sudo apt update && touch /tmp/update_done)",
      # check if apache is installed or not
      "if ! pidof apache2 > /dev/null; then sudo apt install -y apache2; fi" ,
      # Create / update the welcome.html file
      "echo '<h1>Welcome to the Web Server ${aws_instance.ec2[count.index].tags.Name}!</h1>' | sudo tee /var/www/html/welcome.html",
      "sudo systemctl start apache2",
      "sudo systemctl enable apache2"
    ]

    connection {
      type     = "ssh"
      user     = "ubuntu"
      password = var.admin_password
      host     = aws_instance.ec2[count.index].public_ip
      timeout  = "1m"
    }
  }
}
