---
source_image: page_311.png
page_number: 311
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.94
tokens: 7376
characters: 1683
timestamp: 2025-12-24T03:09:04.133985
finish_reason: stop
---

Следующие три шага — уже привычные нам при выделении ресурсов с помощью Terraform terraform init, terraform plan и terraform apply.

В данном случае шаг terraform apply занимает почти 23 минуты. Выделение раздачи Amazon CloudFront — одна из самых длительных операций в AWS, поскольку «за кулисами» Amazon развёртывает раздачу глобально.

Создание записи DNS Route 53

Следующий модуль предназначен для создания записи DNS Route 53 для основного домена сайта www.devops4all.dev. Создайте каталог modules/route53, содержащий два файла: main.tf и variables.tf. Файл main.tf в каталоге route53 указывает Terraform создать запись DNS Route 53 типа A в качестве псевдонима для имени DNS конечной точки CloudFront. В нем используется несколько переменных, объявленных в файле variables.tf, значения которых передаются туда вызывающей модуль стороной:

$ cat modules/route53/main.tf
resource "aws_route53_record" "www" {
  zone_id = "${var.zone_id}"
  name = "www.${var.domain_name}"
  type = "A"
  alias {
    name   = "${var.cloudfront_domain_name}"
    zone_id = "${var.cloudfront_zone_id}"
    evaluate_target_health = false
  }
}

$ cat modules/route53/variables.tf
variable "domain_name" {}
variable "zone_id" {}
variable "cloudfront_domain_name" {}
variable "cloudfront_zone_id" {}

Добавляем ссылку на модуль route53 в файл main.tf Terraform. Передаем zone_id, cloudfront_domain_name и cloudfront_zone_id в модуль route53 в качестве входных переменных. Значение zone_id объявлено в файле variables.tf, а остальные значения извлекаются из выходных результатов модуля cloudfront:

$ cat main.tf
provider "aws" {
  region = "${var.aws_region}"
}

module "s3" {
  source = "./modules/s3"