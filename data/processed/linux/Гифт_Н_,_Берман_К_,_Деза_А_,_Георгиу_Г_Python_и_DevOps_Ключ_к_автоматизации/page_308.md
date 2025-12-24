---
source_image: page_308.png
page_number: 308
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.02
tokens: 7285
characters: 1376
timestamp: 2025-12-24T03:08:49.752314
finish_reason: stop
---

В результате выводится идентификатор ARN сертификата, служащий далее входной переменной для других модулей:

$ cat modules/acm/main.tf
resource "aws_acm_certificate" "certificate" {
  domain_name = "*.${var.domain_name}"
  validation_method = "DNS"
  subject_alternative_names = ["*.${var.domain_name}"]
}

$ cat modules/acm/variables.tf
variable "domain_name" {}

$ cat modules/acm/outputs.tf
output "certificate_arn" {
  value = "${aws_acm_certificate.certificate.arn}"
}

Добавляем в файл main.tf Terraform ссылку на новый модуль acm:

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

Следующие три шага — такие же, как и в последовательности создания корзины S3: terraform init, terraform plan и terraform apply.

Воспользуемся консолью AWS для добавления необходимых для процесса проверки записей Route 53. Проверка и выпуск сертификата обычно занимают несколько минут.

Выделение раздачи Amazon CloudFront

Следующий модуль предназначен для выделения раздачи Amazon CloudFront. Создайте каталог modules/cloudfront, содержащий три файла: main.tf, variables.tf и outputs.tf. Файл main.tf в каталоге cloudfront указывает Terraform создать ресурс раздачи Amazon CloudFront. В нем используются не-