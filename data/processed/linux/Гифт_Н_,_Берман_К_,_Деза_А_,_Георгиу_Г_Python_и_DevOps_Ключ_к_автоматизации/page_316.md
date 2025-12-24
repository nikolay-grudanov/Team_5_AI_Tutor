---
source_image: page_316.png
page_number: 316
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.13
tokens: 7272
characters: 1284
timestamp: 2025-12-24T03:09:08.533783
finish_reason: stop
---

Сгенерированный Pulumi в виде части шаблона aws-python файл __main__.py выглядит следующим образом:

$ cat __main__.py
import pulumi
from pulumi_aws import s3

# Создаем ресурс AWS (корзину S3)
bucket = s3.Bucket('my-bucket')

# Экспорт названия корзины
pulumi.export('bucket_name', bucket.id)

Клонируем на локальную машину репозиторий GitHub примеров Pulumi (https://oreil.ly/SIT-v), после чего копируем файл __main__.py из pulumi-examples/aws-ru-s3-folder в текущий каталог.

Вот новый файл __main__.py в этом каталоге:

$ cat __main__.py
import json
import mimetypes
import os

from pulumi import export, FileAsset
from pulumi_aws import s3

web_bucket = s3.Bucket('s3-website-bucket', website={
    "index_document": "index.html"
})

content_dir = "www"
for file in os.listdir(content_dir):
    filepath = os.path.join(content_dir, file)
    mime_type, _ = mimetypes.guess_type(filepath)
    obj = s3.BucketObject(file,
        bucket=web_bucket.id,
        source=FileAsset(filepath),
        content_type=mime_type)

def public_read_policy_for_bucket(bucket_name):
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
