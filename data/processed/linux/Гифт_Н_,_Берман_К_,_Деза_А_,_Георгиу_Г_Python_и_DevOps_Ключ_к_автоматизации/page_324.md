---
source_image: page_324.png
page_number: 324
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.52
tokens: 7269
characters: 1311
timestamp: 2025-12-24T03:09:12.134126
finish_reason: stop
---

```python
'responsePagePath': "/404.html" },
],
restrictions={
    'geoRestriction': {
        'restrictionType': "none",
    },
},
viewer_certificate={
    'acmCertificateArn': cert_arn,
    'sslSupportMethod': "sni-only",
},
logging_config={
    'bucket': log_bucket.bucket_domain_name,
    'includeCookies': False,
    'prefix': domain_name,
})
```

Осталось запустить pulumi up для выделения раздачи CloudFront.

Создание записи DNS Route 53 для URL сайта

Последний шаг комплексного выделения ресурсов для стека staging представляет собой относительно простую задачу указания записи DNS типа A в качестве псевдонима для домена конечной точки CloudFront:

site_dns_record = route53.Record(
    'site-dns-record',
    name=subdomain,
    zone_id=zone.id,
    type="A",
    aliases=[
        {
            'name': cloudfront_distro.domain_name,
            'zoneId': cloudfront_distro.hosted_zone_id,
            'evaluateTargetHealth': True
        }
    ]
)

Как обычно, выполняем команду pulumi up.

Теперь можно зайти по адресу https://staging.devops4all.dev и увидеть загруженные в S3 файлы. Перейдите в корзину журналирования в консоли AWS и убедитесь в наличии там журналов CloudFront.

Теперь посмотрим, как развернуть тот же самый проект Pulumi в новой среде, которой соответствует новый стек Pulumi.