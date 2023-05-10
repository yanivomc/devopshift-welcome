# docker-bake.dev.hcl
group "default" {
  targets = ["db", "webapp-dev"]
}

target "webapp-dev" {
  dockerfile = "./webapp/Dockerfile"
  tags = ["docker.io/avishayd/webapp"]
}

target "webapp-release" {
  inherits = ["webapp-dev"]
}

target "db" {
  dockerfile = "./db/Dockerfile"
  tags = ["docker.io/avishayd/db"]
}