group "default" {
  targets = ["db", "webapp"]
}

target "webapp" {
  dockerfile = "webapp/Dockerfile"
  tags = ["vladimishiev/webapp"]
}

target "db" {
  dockerfile = "db/Dockerfile"
  tags = ["vladimishiev/db"]
}