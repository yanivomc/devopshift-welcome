target "webapp" {
  dockerfile = "webapp/Dockerfile"
  tags = ["docker.io/talt/webapp"]
}

target "db" {
  dockerfile = "db/Dockerfile"
  tags = ["docker.io/talt/db"]
}