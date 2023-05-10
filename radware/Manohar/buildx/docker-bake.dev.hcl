# docker-bake.dev.hcl
group "default" {
  targets = ["db", "webapp"]
}

target "webapp" {
  dockerfile = "./webapp/Dockerfile"
  tags = ["manoharram/webapp"]
}

target "webapp-release" {
  inherits = ["webapp"]
}

target "db" {
  dockerfile = "./db/Dockerfile"
  tags = ["manoharram/db"]
}
