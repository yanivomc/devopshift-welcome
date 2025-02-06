
module "gal_demo" {
  source = "git::https://github.com/gald10102/devopshift-welcome.git//labs/labmodule/modules?ref=workshop/terraform"
  ami = "ami-0c02fb55956c7d316"
  machine_type = "t2.micro"
  machine_name = "yanivomc"
}


# Gal env:
# folder labs/labmodule/modules
# git: https://github.com/gald10102/devopshift-welcome.git


output "priting_gal_outputs" {
    value = module.gal_demo
  
}

