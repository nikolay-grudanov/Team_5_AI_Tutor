---
source_image: page_305.png
page_number: 305
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.59
tokens: 7257
characters: 1193
timestamp: 2025-12-24T03:08:45.361369
finish_reason: stop
---

{
    "Version":"2012-10-17",
    "Statement":[
        {
            "Sid":"AddPerm",
            "Effect":"Allow",
            "Principal": "*",
            "Action":["s3:GetObject"],
            "Resource":["arn:aws:s3:::www.${var.domain_name}/*"]
        }
    ]
}
POLICY

    website {
        index_document = "index.html"
    }
}

$ cat modules/s3/variables.tf
variable "domain_name" {}

$ cat modules/s3/outputs.tf
output "s3_www_website_endpoint" {
    value = "${aws_s3_bucket.www.website_endpoint}"
}

Атрибут policy вышеупомянутого ресурса aws_s3_bucket представляет собой пример политики корзин S3, открывающей общий доступ к корзине. Если вы работаете с корзинами S3 в контексте IaC, вам не помешает познакомиться с официальной документацией AWS по корзинам и пользовательским политикам (https://oreil.ly/QtTYd).

Основной сценарий Terraform, связывающий воедино все модули, — это файл main.tf в текущем каталоге:

$ cat main.tf
provider "aws" {
    region = "${var.aws_region}"
}

module "s3" {
    source = "./modules/s3"
    domain_name = "${var.domain_name}"
}

Он ссылается на переменные, описанные в отдельном файле variables.tf:

$ cat variables.tf
variable "aws_region" {