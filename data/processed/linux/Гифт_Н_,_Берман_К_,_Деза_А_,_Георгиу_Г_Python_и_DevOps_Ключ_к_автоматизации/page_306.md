---
source_image: page_306.png
page_number: 306
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.60
tokens: 7268
characters: 1353
timestamp: 2025-12-24T03:08:45.535845
finish_reason: stop
---

default = "us-east-1"
}

variable "domain_name" {
    default = "devops4all.dev"
}

Вот дерево текущего каталога на данный момент:

|____main.tf
|____variables.tf
|____modules
|   |____s3
|   |   |____outputs.tf
|   |   |____main.tf
|   |   |____variables.tf

Первый шаг запуска Terraform — вызов команды terraform init для чтения содержимого всех модулей, на которые ссылается файл main.

Следующий шаг — выполнение команды terraform plan, создающей вышеупомянутый эскиз.

Для создания указанных в эскизе ресурсов выполните команду terraform apply:

$ terraform apply

An execution plan has been generated and is shown below.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

# module.s3.aws_s3_bucket.www will be created
+ resource "aws_s3_bucket" "www" {
    + acceleration_status = (known after apply)
    + acl = "public-read"
    + arn = (known after apply)
    + bucket = "www.devops4all.dev"
    + bucket_domain_name = (known after apply)
    + bucket_regional_domain_name = (known after apply)
    + force_destroy = false
    + hosted_zone_id= (known after apply)
    + id= (known after apply)
    + policy = jsonencode(
        {
            + Statement = [
                + {
                    + Action = [
                        + "s3:GetObject",
                    ]
