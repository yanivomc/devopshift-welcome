variable "message" {
    
}


output "publicip" {
    value = "the public ip is : ${var.message}."
  
}

output "anotehermessage" {
    value = "this is another message"
  
}