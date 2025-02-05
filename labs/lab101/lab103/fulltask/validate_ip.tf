resource "time_sleep" "wait_for_ip" {
 create_duration = "1m"  # Wait for 1 minute to allow AWS to allocate the IP
}

resource "null_resource" "validate_ip" {
 provisioner "local-exec" {
   command = <<EOT
     retries=4
     interval=30
     for i in $(seq 1 $retries); do
       if [ -z "${aws_instance.vm.public_ip}" ]; then
         echo "Attempt $i: Public IP address not assigned yet, retrying in $interval seconds..."
         sleep $interval
       else
         echo "Public IP address assigned: ${aws_instance.vm.public_ip}"
         exit 0
       fi
     done
     echo "ERROR: Public IP address was not assigned after $retries attempts." >&2
     exit 1
   EOT
 }
 depends_on = [time_sleep.wait_for_ip]
}
