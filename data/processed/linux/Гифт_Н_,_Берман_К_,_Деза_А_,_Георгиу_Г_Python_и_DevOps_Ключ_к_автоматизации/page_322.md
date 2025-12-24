---
source_image: page_322.png
page_number: 322
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.97
tokens: 7435
characters: 1916
timestamp: 2025-12-24T03:09:23.768634
finish_reason: stop
---

Безрезультатно. Команда pulumi up возвращает ошибку:

AttributeError: 'dict' object has no attribute 'resource_record_name'

Это нас изрядно озадачило, поскольку документация по SDK Python не содержит настолько подробной информации. Мы не знали, какие атрибуты необходимо задавать для объекта domain_validation_options.

Справиться с этой ситуацией нам удалось лишь тогда, когда мы добавили объект domain_validation_options в список экспортов Pulumi, выводимый Pulumi в консоль в конце операции pulumi up:

export('domain_validation_options', domain_validation_options)

В результате команда pulumi up вывела следующее:

+ domain_validation_options: {
    + domain_name      : "staging.devops4all.dev"
    + resourceRecordName : "_c5f82e0f032d0f4f6c7de17fc2c.staging.devops4all.dev."
    + resourceRecordType : "CNAME"
    + resourceRecordValue: "_08e3d475bf3aeda0c98.ltfvzjuylp.acm-validations.aws."
}

В точку! Оказалось, что атрибуты объекта domain_validation_options остались в верблюжьем регистре.

Вот вторая, удачная попытка переноса на Python:

cert_validation_record = route53.Record(
    'cert-validation-record',
    name=domain_validation_options['resourceRecordName'],
    zone_id=zone.id,
    type=domain_validation_options['resourceRecordType'],
    records=[domain_validation_options['resourceRecordValue']],
    ttl=600)

Далее указываем новый тип выделяемого ресурса — ресурс завершения проверки сертификата. В результате операция pulumi up ждет, пока ACM завершит проверку сертификата, обратившись к созданной ранее записи проверки Route 53:

cert_validation_completion = acm.CertificateValidation(
    'cert-validation-completion',
    certificate_arn=cert.arn,
    validation_record_fqdns=[cert_validation_dns_record.fqdn])

cert_arn = cert_validation_completion.certificate_arn

Теперь у нас есть полностью автоматизированный способ создания SSL-сертификата ACM, а также проверки его через DNS.