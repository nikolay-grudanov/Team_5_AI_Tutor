---
source_image: page_309.png
page_number: 309
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.62
tokens: 7292
characters: 1372
timestamp: 2025-12-24T03:08:49.766907
finish_reason: stop
---

сколько переменных, объявленных в файле variables.tf, значения которых передаются туда вызывающей модуль стороной. В результате выводятся доменное имя DNS для конечной точки CloudFront и идентификатор зоны хостинга Route 53 для раздачи, служащие в дальнейшем входными переменными для других модулей:

$ cat modules/cloudfront/main.tf
resource "aws_cloudfront_distribution" "www_distribution" {
  origin {
    custom_origin_config {
      // These are all the defaults.
      http_port= "80"
      https_port  = "443"
      origin_protocol_policy = "http-only"
      origin_ssl_protocols= ["TLSv1", "TLSv1.1", "TLSv1.2"]
    }

    domain_name = "${var.s3_www_website_endpoint}"
    origin_id= "www.${var.domain_name}"
  }

  enabled  = true
  default_root_object = "index.html"

  default_cache_behavior {
    viewer_protocol_policy = "redirect-to-https"
    compress = true
    allowed_methods= ["GET", "HEAD"]
    cached_methods = ["GET", "HEAD"]
    target_origin_id = "www.${var.domain_name}"
    min_ttl  = 0
    default_ttl = 86400
    max_ttl  = 31536000

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }
  }

  aliases = ["www.${var.domain_name}"]

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    acm_certificate_arn = "${var.acm_certificate_arn}"