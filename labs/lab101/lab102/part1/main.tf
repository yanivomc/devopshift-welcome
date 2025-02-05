variable "emptyip" {
    default = "192.168.1.1"
}

resource "null_resource" "check_If_empty_ip" {
  provisioner "local-exec" {
    command = <<EOT
      if [ -z "${var.emptyip}" ]; then
        echo "ERROR: Public IP address was not assigned." >&2
        exit 1
      fi
    EOT
  }
}
