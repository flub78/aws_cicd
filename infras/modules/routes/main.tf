# resource block for elastic ip #
resource "aws_eip" "web_server_eip" {
  instance = var.server_id
  vpc = true
  tags = {
    Name = "${var.basename}_eip"
  }
}

# resource for route53 zone #
data "aws_route53_zone" "primary" {
  name = var.domain
}

# resource for route53 record #
resource "aws_route53_record" "root" {
  zone_id = data.aws_route53_zone.primary.zone_id
  name    = "${var.subdomain}.${var.domain}"
  type    = "A"

  ttl    = "300"
  records = [aws_eip.web_server_eip.public_ip]
}
