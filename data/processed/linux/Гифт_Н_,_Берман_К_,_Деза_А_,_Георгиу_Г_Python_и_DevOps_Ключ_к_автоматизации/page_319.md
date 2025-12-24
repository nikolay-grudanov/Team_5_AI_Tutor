---
source_image: page_319.png
page_number: 319
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.88
tokens: 7331
characters: 1485
timestamp: 2025-12-24T03:09:12.257289
finish_reason: stop
---

Создание значений параметров конфигурации для стека staging

Наш текущий стек — staging. Переименуем существующий каталог www в www-staging, после чего с помощью команды pulumi config set зададим значения двух параметров конфигурации для текущего стека staging: domain_name и local_webdir:

(venv) mv www www-staging
(venv) pulumi config set local_webdir www-staging
(venv) pulumi config set domain_name staging.devops4all.dev

Больше подробностей о том, как Pulumi обращается со значениями параметров конфигурации и секретными данными, вы можете найти в справочной документации Pulumi (https://oreil.ly/D_Cy5).

Для просмотра имеющихся значений параметров конфигурации для текущего стека выполняем:

(venv) pulumi config
KEY        VALUE
aws:region us-east-1
domain_name staging.devops4all.dev
local_webdir www-staging

Задав значения параметров конфигурации, воспользуемся ими в коде Pulumi:

import pulumi

config = pulumi.Config('proj1')  # proj1 is project name defined in Pulumi.yaml

content_dir = config.require('local_webdir')
domain_name = config.require('domain_name')

Теперь значения параметров конфигурации заданы, далее создадим SSL-сертификат с помощью сервиса AWS Certificate Manager.

Создаем SSL-сертификат ACM

В этом месте становится заметно, что Pulumi несколько сыровата в том, что касается SDK Python. Просто прочитать руководство Pulumi по Python SDK для модуля acm (https://oreil.ly/Niwaj) недостаточно, чтобы разобраться, что нужно делать в программе Pulumi.