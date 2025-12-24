---
source_image: page_326.png
page_number: 326
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.22
tokens: 7364
characters: 1524
timestamp: 2025-12-24T03:09:23.981077
finish_reason: stop
---

Do you want to perform this update? yes
Updating (prod):

Type                Name                Status
pulumi:pulumi:Stack proj1-prod
+   aws:cloudfront:Distribution cloudfront-distro created
+   aws:route53:Record           site-dns-record created

Outputs:
+ cloudfront_domain: "d3uhgbdw67nmlc.cloudfront.net"
+ log_bucket_id      : "cdn-log-bucket-53d8ea3"
+ web_bucket_id      : "s3-website-bucket-cde"
+ website_url        : "s3-website-bucket-cde.s3-website-us-east-1.amazonaws.com"

Resources:
    + 2 created
    10 unchanged

Duration: 18m54s

Успешно! Стек prod полностью развернут.

Однако содержимое каталога www-prod со статическими файлами нашего сайта в настоящий момент идентично содержимому каталога www-staging.

Отредактируем файл www-prod/index.html, поменяв «Hello, S3!» на «Hello, S3 production!», после чего снова запустим pulumi up, чтобы подхватить изменения и загрузить модифицированный файл в S3:

(venv) pulumi up
Previewing update (prod):

Type                Name                Plan    Info
pulumi:pulumi:Stack proj1-prod
~   aws:s3:BucketObject index.html     update  [diff: ~source]

Resources:
    ~ 1 to update
    11 unchanged

Do you want to perform this update? yes
Updating (prod):

Type                Name                Status   Info
pulumi:pulumi:Stack proj1-prod
~   aws:s3:BucketObject index.html     updated  [diff: ~source]

Outputs:
cloudfront_domain: "d3uhgbdw67nmlc.cloudfront.net"
log_bucket_id      : "cdn-log-bucket-53d8ea3"
web_bucket_id      : "s3-website-bucket-cde"