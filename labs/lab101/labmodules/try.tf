module "myoutput1" {
  source = "./modules/ec2"
  ami = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"

}

output "printinfo" {
  value = module.myoutput1
}

