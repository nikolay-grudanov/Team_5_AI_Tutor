---
source_image: page_476.png
page_number: 476
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.32
tokens: 7421
characters: 1906
timestamp: 2025-12-24T03:13:16.300701
finish_reason: stop
---

YAML

YAML постепенно становится стандартом для связанных с DevOps файлов конфигурации. YAML — удобный для восприятия человеком формат сериализации данных, представляющий собой расширение JSON. Название его расшифровывается как YAML Ain’t Markup Language («YAML — это не язык разметки»). YAML можно нередко встретить в таких системах сборки, как AWS CodePipeline (https://oreil.ly/WZnIl), CircleCI (https://oreil.ly/0r8cK), и таких вариантах PaaS, как Google App Engine (https://oreil.ly/ny_TD).

YAML используется так широко вовсе не случайно, а вследствие потребности в языке конфигурации с возможностью быстрых итераций при взаимодействии с высокоавтоматизированными системами. Как программисту, так и обычному пользователю интуитивно ясно, как редактировать эти файлы. Вот пример:

import yaml

kubernetes_components = {
    "Pod": "Basic building block of Kubernetes.",
    "Service": "An abstraction for dealing with Pods.",
    "Volume": "A directory accessible to containers in a Pod.",
    "Namespaces": "A way to divide cluster resources between users."
}

with open("kubernetes_info.yaml", "w") as yaml_to_write:
    yaml.safe_dump(kubernetes_components, yaml_to_write, default_flow_style=False)

Записанный на диск результат выглядит следующим образом:

cat kubernetes_info.yaml

Namespaces: A way to divide cluster resources between users.
Pod: Basic building block of Kubernetes.
Service: An abstraction for dealing with Pods.
Volume: A directory accessible to containers in a Pod.

Отсюда ясно, насколько просто сериализовать структуру данных Python в удобный для редактирования и итеративной обработки формат. Чтение этого файла также требует всего двух строк кода:

import yaml

with open("kubernetes_info.yaml", "rb") as yaml_to_read:
    result = yaml.safe_load(yaml_to_read)

А далее можно вывести результаты во вполне аккуратном виде:

import pprint
pp = pprint.PrettyPrinter(indent=4)