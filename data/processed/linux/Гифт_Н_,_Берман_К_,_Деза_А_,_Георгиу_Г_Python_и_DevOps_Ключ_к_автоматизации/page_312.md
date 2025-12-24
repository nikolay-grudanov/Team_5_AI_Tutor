---
source_image: page_312.png
page_number: 312
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.92
tokens: 7379
characters: 1601
timestamp: 2025-12-24T03:09:04.201720
finish_reason: stop
---

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
module "route53" {
  source = "./modules/route53"
  domain_name = "${var.domain_name}"
  zone_id = "${var.zone_id}"
  cloudfront_domain_name = "${module.cloudfront.domain_name}"
  cloudfront_zone_id = "${module.cloudfront.hosted_zone_id}"
}
$ cat variables.tf
variable "aws_region" {
  default = "us-east-1"
}
variable "domain_name" {
  default = "devops4all.dev"
}
variable "zone_id" {
  default = "ZWX18ZIVHAA50"
}

Следующие три шага, надеемся, вам уже привычные, предназначены для выделения ресурсов с помощью Terraform: terraform init, terraform plan и terraform apply.

Копирование статических файлов в корзину S3

Для комплексного тестирования выделенного статического веб-сайта создайте простой файл index.html, содержащий JPEG-изображение, и скопируйте оба файла в выделенную ранее с помощью Terraform корзину S3. Убедитесь, что значение переменной среды AWS_PROFILE соответствует уже указанному в файле ~/.aws/credentials:

$ echo $AWS_PROFILE
gheorghiu-net
$ aws s3 cp static_files/index.html s3://www.devops4all.dev/index.html
upload: static_files/index.html to s3://www.devops4all.dev/index.html
$ aws s3 cp static_files/devops4all.jpg s3://www.devops4all.dev/devops4all.jpg
upload: static_files/devops4all.jpg to s3://www.devops4all.dev/devops4all.jpg