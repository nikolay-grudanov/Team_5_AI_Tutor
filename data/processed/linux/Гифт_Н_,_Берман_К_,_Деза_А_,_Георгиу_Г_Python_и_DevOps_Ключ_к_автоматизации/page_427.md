---
source_image: page_427.png
page_number: 427
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.41
tokens: 7533
characters: 1741
timestamp: 2025-12-24T03:12:13.789568
finish_reason: stop
---

Меняем также значение checked на True, поскольку мы уже видели сообщение, которое хотим обновить:

ExpressionAttributeValues={
    ':text': data['text'],
    ':checked': True,
    ':updatedAt': timestamp,
},

Снова развертываем стек с помощью команды cdk deploy.

Проверяем обновление элемента todo с помощью curl:

$ curl -X \
PUT https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/prod/todos/58a992c6-cdb4-11e9-9a8f-9ed29c44196e \
--data '{ "text": "Learn CDK with Python by reading the PyForDevOps book"}' '{"checked": true, "createdAt": "1567451007.680936", "text": "Learn CDK with Python by reading the PyForDevOps book", "id": "58a992c6-cdb4-11e9-9a8f-9ed29c44196e", "updatedAt": 1567453288764}%'

Выводим список элементов todo, чтобы проверить, как прошло обновление:

$ curl https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/prod/todos | jq [
{
    "checked": true,
    "createdAt": "1567451007.680936",
    "text": "Learn CDK with Python by reading the PyForDevOps book",
    "id": "58a992c6-cdb4-11e9-9a8f-9ed29c44196e",
    "updatedAt": 1567453288764
}
]

Следующий шаг — выделение контейнеров AWS Fargate для нагрузочного тестирования только что развернутого нами API REST. Каждый контейнер представляет собой запущенный образ Docker, использующий фреймворк автоматизации тестирования Taurus (https://oreil.ly/OGDne) для запуска утилиты нагрузочного тестирования Molotov (https://oreil.ly/OGDne). Мы уже рассказывали о Molotov — простой и очень удобной утилите нагрузочного тестирования на основе Python — в главе 5.

Начнем с создания Dockerfile для запуска Taurus и Molotov в каталоге loadtest:

$ mkdir loadtest; cd loadtest
$ cat Dockerfile
FROM blazemeter/taurus
COPY scripts /scripts
COPY taurus.yaml /bzt-configs/