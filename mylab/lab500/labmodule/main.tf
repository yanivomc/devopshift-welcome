module "outputdemo1" {
    source = "./modules/outputdemo"
    ec2info = "createmachine"
}





output "printingmpduleinfo" {
    value = module.outputdemo1
  
}