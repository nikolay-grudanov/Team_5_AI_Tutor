---
source_image: page_317.png
page_number: 317
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.57
tokens: 7361
characters: 1649
timestamp: 2025-12-24T03:09:12.019050
finish_reason: stop
---

```python
"Resource": [
    f"arn:aws:s3:::{bucket_name}/*",
]
})

bucket_name = web_bucket.id
bucket_policy = s3.BucketPolicy("bucket-policy",
    bucket=bucket_name,
    policy=bucket_name.apply(public_read_policy_for_bucket))

# Экспорт названия корзины
export('bucket_name', web_bucket.id)
export('website_url', web_bucket.website_endpoint)

Обратите внимание на использование переменных Python для content_dir и bucket_name, использование цикла for, а также обычной функции Python public_read_policy_for_bucket. Так приятно иметь возможность применять обычные конструкции языка Python в программах IaC!

Пришло время запустить pulumi up, чтобы выделить указанные в файле __main__.py ресурсы. Эта команда отображает все создаваемые ресурсы. Выбираем вариант yes, чтобы запустить процесс выделения ресурсов:

(venv) pulumi up
Previewing update (staging):

    Type                Name                Plan
+ pulumi:pulumi:Stack proj1-staging       create
+   ├── aws:s3:Bucket s3-website-bucket   create
+   ├── aws:s3:BucketObject favicon.png   create
+   ├── aws:s3:BucketPolicy bucket-policy create
+   ├── aws:s3:BucketObject python.png    create
+   └── aws:s3:BucketObject index.html    create

Resources:
    + 6 to create

Do you want to perform this update? yes
Updating (staging):

    Type                Name                Status
+ pulumi:pulumi:Stack proj1-staging       created
+   ├── aws:s3:Bucket s3-website-bucket   created
+   ├── aws:s3:BucketObject index.html    created
+   ├── aws:s3:BucketObject python.png    created
+   ├── aws:s3:BucketObject favicon.png   created
+   └── aws:s3:BucketPolicy bucket-policy  created
```