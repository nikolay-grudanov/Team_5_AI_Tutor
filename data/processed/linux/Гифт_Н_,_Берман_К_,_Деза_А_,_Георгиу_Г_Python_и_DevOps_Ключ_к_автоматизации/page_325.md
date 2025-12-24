---
source_image: page_325.png
page_number: 325
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.69
tokens: 7427
characters: 1679
timestamp: 2025-12-24T03:09:27.035447
finish_reason: stop
---

Создание и развертывание нового стека

Мы решили модифицировать нашу программу Pulumi так, чтобы она не выделяла новую зону Route 53, а использовала значение идентификатора уже существующей зоны из параметра конфигурации.

Для создания стека prod применим команду pulumi stack init, указав в качестве названия prod:

(venv) pulumi stack init
Please enter your desired stack name: prod
Created stack 'prod'

В списке стеков теперь два стека, staging и prod со звездочкой, означающей, что этот стек является текущим:

(venv) pulumi stack ls
NAME      LAST UPDATE   RESOURCE COUNT   URL
prod*     n/a           n/a              https://app.pulumi.com/griggheo/proj1/prod
staging   14 minutes ago 14              https://app.pulumi.com/griggheo/proj1/staging

Пришло время задать подходящие значения параметров конфигурации для стека prod. Воспользуемся новым параметром конфигурации dns_zone_id со значением, равным идентификатору зоны, уже созданной Pulumi при выделении стека staging:

(venv) pulumi config set aws:region us-east-1
(venv) pulumi config set local_webdir www-prod
(venv) pulumi config set domain_name www.devops4all.dev
(venv) pulumi config set dns_zone_id Z2FTL2X8M0EBTW

Меняем код так, чтобы читать значение zone_id из конфигурации, а не создавать объект зоны Route 53.

Выделяем ресурсы AWS с помощью команды pulumi up:

(venv) pulumi up
Previewing update (prod):

    Type                                 Name                Plan
    pulumi:pulumi:Stack                  proj1-prod
+   ├── aws:cloudfront:Distribution    cloudfront-distro   create
+   └── aws:route53:Record             site-dns-record     create

Resources:
    + 2 to create
    10 unchanged