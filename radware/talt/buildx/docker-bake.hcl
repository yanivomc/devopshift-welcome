target "webapp" {
  dockerfile = "webapp/Dockerfile"
  tags = ["docker.io/username/webapp"]
}

target "db" {
  dockerfile = "db/Dockerfile"
  tags = ["docker.io/username/db"]
}