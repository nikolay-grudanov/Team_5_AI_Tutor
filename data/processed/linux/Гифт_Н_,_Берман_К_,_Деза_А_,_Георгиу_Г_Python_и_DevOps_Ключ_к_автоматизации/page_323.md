---
source_image: page_323.png
page_number: 323
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.34
tokens: 7313
characters: 1524
timestamp: 2025-12-24T03:09:12.159891
finish_reason: stop
---

Следующий этап — выделение раздачи CloudFront на корзину S3, где размещены статические файлы для нашего сайта.

Выделение раздачи CloudFront

Воспользуемся руководством SDK для модуля cloudfront (https://oreil.ly/4n98-), чтобы разобраться, какие параметры конструктора необходимо передавать в cloudfront.Distribution. Выясним, какими должны быть значения этих параметров, изучив внимательно код на TypeScript.

Вот конечный результат:

log_bucket = s3.Bucket('cdn-log-bucket', acl='private')

cloudfront_distro = cloudfront.Distribution (
    enabled=True,
    aliases=[ domain_name ],
    origins=[
        {
            'originId': web_bucket.arn,
            'domainName': web_bucket.website_endpoint,
            'customOriginConfig': {
                'originProtocolPolicy': "http-only",
                'httpPort': 80,
                'httpsPort': 443,
                'originSslProtocols': ["TLSv1.2"],
            },
        },
    ],
    default_root_object="index.html",
    default_cache_behavior={
        'targetOriginId': web_bucket.arn,

        'viewerProtocolPolicy': "redirect-to-https",
        'allowedMethods': ["GET", "HEAD", "OPTIONS"],
        'cachedMethods': ["GET", "HEAD", "OPTIONS"],
        'forwardedValues': {
            'cookies': { 'forward': "none" },
            'queryString': False,
        },

        'minTtl': 0,
        'defaultTtl': 600,
        'maxTtl': 600,
    },
    price_class="PriceClass_100",
    custom_error_responses=[
        { 'errorCode': 404, 'responseCode': 404,