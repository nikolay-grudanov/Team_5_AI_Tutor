---
source_image: page_320.png
page_number: 320
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.45
tokens: 7400
characters: 1692
timestamp: 2025-12-24T03:09:17.874774
finish_reason: stop
---

К счастью, существует множество примеров Pulumi на TypeScript, из которых можно почерпнуть вдохновение. Один из таких примеров, прекрасно иллюстрирующий наш сценарий использования, — aws-ts-static-website (https://oreil.ly/7F39c).

Вот код TypeScript для создания нового сертификата ACM (из файла index.ts (https://oreil.ly/mlSr1)):

const certificate = new aws.acm.Certificate("certificate", {
    domainName: config.targetDomain,
    validationMethod: "DNS",
}, { provider: eastRegion });

А вот написанный нами эквивалентный код на языке Python:

from pulumi_aws import acm

cert = acm.Certificate('certificate', domain_name=domain_name,
    validation_method='DNS')

Эмпирическое правило по переносу кода Pulumi с TypeScript на Python: названия параметров в верблюжьем регистре в языке Python необходимо преобразовать в змеиный регистр. Как вы видели в предыдущем примере, domainName при этом превращается в domain_name, а validationMethod — в validation_method.

Следующий этап — выделение зоны Route 53, а в ней — проверочной записи DNS для SSL-сертификата ACM.

Выделение зоны Route 53 и записей DNS

Выделение новой зоны Route 53 с помощью Pulumi не доставляет сложностей, если следовать справочному руководству Pulumi SDK по модулю route53 (https://oreil.ly/cU9Yj):

from pulumi_aws import route53

domain_name = config.require('domain_name')

# Разбиваем доменное имя на имя поддомена и родительского домена,
# например "www.example.com" => "www", "example.com"
def get_domain_and_subdomain(domain):
    names = domain.split(".")
    if len(names) < 3:
        return('', domain)
    subdomain = names[0]
    parent_domain = ".".join(names[1:])
    return (subdomain, parent_domain)