group "default" {
  targets = ["db", "webapp-dev"]
}

target "webapp-dev" {
  dockerfile = "webapp/Dockerfile"
  tags = ["barhorovitz/webapp"]
}

target "webapp-release" {
  inherits = ["webapp-dev"]
  platforms = ["linux/amd64", "linux/arm64"]
}

target "db" {
  dockerfile = "db/Dockerfile"
  tags = ["barhorovitz/db"]
}

