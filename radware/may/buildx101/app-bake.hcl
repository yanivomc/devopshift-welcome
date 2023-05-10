group "default" {
  targets = ["db", "webapp-dev"]
}

target "webapp-dev" {
  dockerfile = "./WEBAPP/Dockerfile"
  tags = ["mayb/webapp"]
}

target "webapp-release" {
  inherits = ["webapp-dev"]
}

target "db" {
  dockerfile = "./DB/Dockerfile"
  tags = ["mayb/db"]
}
