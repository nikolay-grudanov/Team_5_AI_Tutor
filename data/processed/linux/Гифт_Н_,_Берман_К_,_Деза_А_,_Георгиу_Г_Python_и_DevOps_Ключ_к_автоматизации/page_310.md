---
source_image: page_310.png
page_number: 310
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.49
tokens: 7301
characters: 1440
timestamp: 2025-12-24T03:08:57.302685
finish_reason: stop
---

```plaintext
    ssl_support_method  = "sni-only"
  }
}

$ cat modules/cloudfront/variables.tf
variable "domain_name" {}
variable "acm_certificate_arn" {}
variable "s3_www_website_endpoint" {}

$ cat modules/cloudfront/outputs.tf
output "domain_name" {
  value = "${aws_cloudfront_distribution.www_distribution.domain_name}"
}

output "hosted_zone_id" {
  value = "${aws_cloudfront_distribution.www_distribution.hosted_zone_id}"
}

Добавляем ссылку на модуль cloudfront в файл main.tf Terraform. Передаем s3_www_website_endpoint и acm_certificate_arn в модуль cloudfront в качестве входных переменных. Их значения извлекаются из выходных результатов других модулей, s3 и acm соответственно.

ARN расшифровывается как Amazon Resource Name («имя ресурса Amazon») и представляет собой строковое значение, однозначно идентифицирующее данный ресурс AWS. При использовании утилит IaC, производящих действия внутри AWS, вы увидите немало генерируемых и передаваемых в виде переменных значений ARN.

$ cat main.tf
provider "aws" {
  region = "${var.aws_region}"
}

module "s3" {
  source = "./modules/s3"
  domain_name = "${var.domain_name}"
}

module "acm" {
  source = "./modules/acm"
  domain_name = "${var.domain_name}"
}

module "cloudfront" {
  source = "./modules/cloudfront"
  domain_name = "${var.domain_name}"
  s3_www_website_endpoint = "${module.s3.s3_www_website_endpoint}"
  acm_certificate_arn = "${module.acm.certificate_arn}"
}
```