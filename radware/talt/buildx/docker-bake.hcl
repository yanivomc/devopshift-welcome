target "webapp" {
  dockerfile = "webapp/Dockerfile"
  tags = ["a1cor/webapp"]
}

target "db" {
  dockerfile = "db/Dockerfile"
  tags = ["a1cor/db"]
}