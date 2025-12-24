---
source_image: page_318.png
page_number: 318
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.80
tokens: 7426
characters: 1621
timestamp: 2025-12-24T03:09:17.377581
finish_reason: stop
---

Outputs:
    bucket_name: "s3-website-bucket-8e08f8f"
    website_url: "s3-website-bucket-8e08f8f.s3-website-us-east-1.amazonaws.com"

Resources:
    + 6 created

Duration: 14s

Просматриваем имеющиеся стеки Pulumi:

(venv) pulumi stack ls
NAME      LAST UPDATE   RESOURCE COUNT   URL
staging*  2 minutes ago 7                https://app.pulumi.com/griggheo/proj1/staging

(venv) pulumi stack
Current stack is staging:
    Owner: griggheo
    Last updated: 3 minutes ago (2019-06-13 22:05:38.088773 -0700 PDT)
    Pulumi version: v0.17.16
Current stack resources (7):
    TYPE                                 NAME
    pulumi:pulumi:Stack                  proj1-staging
    pulumi:providers:aws                 default
    aws:s3/bucket:Bucket                 s3-website-bucket
    aws:s3/bucketPolicy:BucketPolicy     bucket-policy
    aws:s3/bucketObject:BucketObject     index.html
    aws:s3/bucketObject:BucketObject     favicon.png
    aws:s3/bucketObject:BucketObject     python.png

Просматриваем вывод текущего стека:

(venv) pulumi stack output
Current stack outputs (2):
    OUTPUT      VALUE
    bucket_name s3-website-bucket-8e08f8f
    website_url s3-website-bucket-8e08f8f.s3-website-us-east-1.amazonaws.com

Зайдите на URL, приведенный в выводе website_url (http://s3-website-bucket-8e08f8f.s3-website-us-east-1.amazonaws.com/), и убедитесь, что статический сайт доступен.

В следующих разделах мы расширим этот проект Pulumi, задав дополнительные ресурсы AWS для выделения, чтобы выделить то же, что и с помощью Terraform: SSL-сертификат ACM, раздачу CloudFront и запись DNS Route 53 для URL нашего сайта.