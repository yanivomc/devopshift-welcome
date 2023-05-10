group "default" {
  targets = ["db", "webapp"]
}

target "webapp" {
  dockerfile = "webapp/Dockerfile"
  tags = ["ronalon/webapp"]
}

target "webapp-release" {
  inherits = ["webapp"]
}


target "db" {
  dockerfile = "db/Dockerfile"
  tags = ["ronalon/db"]
}