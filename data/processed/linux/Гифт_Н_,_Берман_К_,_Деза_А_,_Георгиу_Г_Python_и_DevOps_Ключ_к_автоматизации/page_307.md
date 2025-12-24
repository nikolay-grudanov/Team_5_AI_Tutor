---
source_image: page_307.png
page_number: 307
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.18
tokens: 7302
characters: 1390
timestamp: 2025-12-24T03:08:49.366082
finish_reason: stop
---

+ Effect = "Allow"
+ Principal = "*"
+ Resource  =
    + "arn:aws:s3:::www.devops4all.dev/*",
]
+ Sid = "AddPerm"
},
]
+ Version= "2012-10-17"
}
+ region  = (known after apply)
+ request_payer = (known after apply)
+ website_domain= (known after apply)
+ website_endpoint = (known after apply)

+ versioning {
    + enabled = (known after apply)
    + mfa_delete = (known after apply)
}

+ website {
    + index_document = "index.html"
}
}

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
Terraform will perform the actions described above.
Only 'yes' will be accepted to approve.

Enter a value: yes

module.s3.aws_s3_bucket.www: Creating...
module.s3.aws_s3_bucket.www: Creation complete after 7s [www.devops4all.dev]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Теперь с помощью UI веб-консоли AWS можно убедиться, что корзина S3 была создана.

Предоставление SSL-сертификата с помощью ACM AWS

Следующий модуль предназначен для предоставления SSL-сертификата с помощью сервиса AWS Certificate Manager. Создайте каталог modules/acm, содержащий три файла: main.tf, variables.tf и outputs.tf. Файл main.tf в каталоге acm указывает Terraform создать SSL-сертификат ACM с DNS в качестве метода проверки. В нем используется объявленная в файле variables.tf переменная domain_name, значение которой передается туда вызывающей модуль стороной.