# docker-bake.hcl
group "build" {
  targets = ["db", "webapp-dev"]
}

target "webapp-dev" {
  dockerfile = "Dockerfile.webapp"
  tags = ["anoojm/webapp"]
}

target "db" {
  dockerfile = "Dockerfile.db"
  tags = ["anoojm/db"]
}