---
source_image: page_321.png
page_number: 321
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.14
tokens: 7394
characters: 1963
timestamp: 2025-12-24T03:09:17.586297
finish_reason: stop
---

(subdomain, parent_domain) = get_domain_and_subdomain(domain_name)
zone = route53.Zone("route53_zone", name=parent_domain)

Предыдущий фрагмент кода демонстрирует разбиение на две части прочитанного в переменную domain_name значения параметра конфигурации с помощью обычных функций Python. Например, domain_name со значением staging.devops4all.dev будет разбито на subdomain (staging) и parent_domain (devops4all.dev).

Переменная parent_domain далее используется в качестве параметра конструктора объекта zone, который указывает Pulumi на необходимость выделить ресурс route53.Zone.

После создания зоны Route 53 необходимо сделать так, чтобы серверы имен Namecheap указывали на серверы имен, прописанные в записи DNS для нашей новой зоны, чтобы она была доступна всем.

До сих пор все было хорошо. Следующий этап — создание сертификата ACM и записи DNS для его проверки.

Сначала мы попытались перенести пример с языка TypeScript, следуя эмпирическому правилу преобразования верблюжьего регистра в змеиный:

TypeScript:
    const certificateValidationDomain = new aws.route53.Record(
        `${config.targetDomain}-validation`, {
            name: certificate.domainValidationOptions[0].resourceRecordName,
            zoneId: hostedZoneId,
            type: certificate.domainValidationOptions[0].resourceRecordType,
            records: [certificate.domainValidationOptions[0].resourceRecordValue],
            ttl: tenMinutes,
        });
    );

Первая попытка преобразования в код на Python путем изменения регистра:

cert = acm.Certificate('certificate',
    domain_name=domain_name, validation_method='DNS')

domain_validation_options = cert.domain_validation_options[0]

cert_validation_record = route53.Record(
    'cert-validation-record',
    name=domain_validation_options.resource_record_name,
    zone_id=zone.id,
    type=domain_validation_options.resource_record_type,
    records=[domain_validation_options.resource_record_value],
    ttl=600)