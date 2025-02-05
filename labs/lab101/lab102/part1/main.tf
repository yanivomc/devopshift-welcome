variable "emptyip" {
    default = "192.168.1.1"
}

# provider "aws" {
#   region = var.region
# }


# variable "region" {
#   default = "us-east-1"
# }

data "aws_instance" "yaniv_vm" {
  instance_id = "i-09df7e0ed385f871b"
}

output "public_ip" {
  value = data.aws_instance.yaniv_vm.public_ip
}
provider "aws" {
    region = "us-east-1"
}

# data "aws_instances" "filtered" {
#   filter {
#     name   = "tag:Name"
#     values = ["yaniv-vm"]
#   }
# }

# output "public_ip" {
#   value = data.aws_instances.filtered.instances[0].public_ip
# }


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
