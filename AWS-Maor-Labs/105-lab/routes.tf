# routes.tf
resource "aws_route_table" "public_rt" {
  vpc_id = module.vpc.vpc_id
  # vpc_id = aws_vpc.lab_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = module.vpc.vpc_cidr
  }
}

resource "aws_route_table_association" "public_assoc" {
  subnet_id      = module.vpc.public_subnet.id
  route_table_id = aws_route_table.public_rt.id
}
