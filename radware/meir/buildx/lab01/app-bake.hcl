group "default" {
  targets = ["db", "webapp"]
}

target "webapp" {
  dockerfile = "webapp/Dockerfile"
  tags = ["assism/webapp"]
}



target "db" {
  dockerfile = "db/Dockerfile"
  tags = ["assism/db"]
}