---
source_image: page_371.png
page_number: 371
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.33
tokens: 7433
characters: 1686
timestamp: 2025-12-24T03:10:44.452994
finish_reason: stop
---

Просматриваем журналы модуля процесса-исполнителя с помощью команды kubectl logs:

$ kubectl logs worker-7dbf5ff56c-hga37
20:43:13 RQ worker 'rq:worker:040640781edd4055a990b798ac2eb52d'
started, version 1.0
20:43:13 *** Listening on default...
20:43:13 Cleaning registries for queue: default

Следующий этап — развертывание приложения. При развертывании приложения в варианте с docker-compose в главе 11 мы использовали отдельный контейнер Docker для запуска миграций, необходимых для обновления базы данных Flask. Подобные задачи хорошо подходят для запуска в виде вспомогательного контейнера в том же модуле, что и основной контейнер приложения. Мы опишем этот вспомогательный контейнер в манифесте развертывания нашего приложения в виде объекта Kubernetes initContainer (https://oreil.ly/80L5L). Контейнер такого типа гарантированно выполняется внутри соответствующего модуля до запуска всех прочих контейнеров из него.

Добавьте следующий раздел в сгенерированный утилитой Kompose файл манифеста app-deployment.yaml и удалите файл migrations-deployment.yaml:

    initContainers:
    - args:
      - manage.py
      - db
      - upgrade
    env:
      - name: APP_SETTINGS
        value: config.ProductionConfig
      - name: DATABASE_URL
        value: postgresql://wordcount_dbadmin:@db/wordcount
    image: griggheo/flask-by-example:v1
    name: migrations
    resources: {}

$ rm migrations-deployment.yaml

Еще раз воспользуемся объектом Secret fbe-secret, созданным для развертывания процесса-исполнителя, в манифесте развертывания приложения:

$ cat app-deployment.yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    kompose.cmd: kompose convert