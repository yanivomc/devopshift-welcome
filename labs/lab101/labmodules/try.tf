module "myoutput1" {
  source = "./modules/ec2"
  ami = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"

}

output "printinfo" {
  value = module.myoutput1
}


variable "enabled_services" {
  type    = list(string)
  default = ["prod"]
}

variable "s3_buckets" {
  type    = set(string)
  default = ["prod", "dev"]
}

resource "aws_s3_bucket" "buckets" {
  for_each = { for key in var.s3_buckets : key => key if contains(var.enabled_services, key) }
  bucket = "my-app-${each.key}"
  acl    = "private"
  tags = {
    Name        = "Bucket for ${each.key}"
    Environment = each.key
  }
}
