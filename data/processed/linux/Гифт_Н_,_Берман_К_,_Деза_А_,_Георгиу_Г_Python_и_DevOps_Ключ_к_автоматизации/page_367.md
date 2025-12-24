---
source_image: page_367.png
page_number: 367
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.90
tokens: 7344
characters: 1448
timestamp: 2025-12-24T03:10:32.137882
finish_reason: stop
---

$ kubectl describe secret fbe-secret
Name:        fbe-secret
Namespace:   default
Labels:      <none>
Annotations: <none>
Type:  Opaque
Data
dbpass:  12 bytes

Для извлечения Secret в кодировке base64 применяем команду:

$ kubectl get secrets fbe-secret -ojson | jq -r ".data.dbpass"
MYPASSBASE64

Для получения пароля в виде открытого текста на машине под управлением macOS можно воспользоваться следующей командой:

$ kubectl get secrets fbe-secret -ojson | jq -r ".data.dbpass" | base64 -D MYPASS

На машине под управлением Linux для декодирования base64 служит флаг -d, так что команда выглядит следующим образом:

$ kubectl get secrets fbe-secret -ojson | jq -r ".data.dbpass" | base64 -d MYPASS

Теперь можно использовать объект Secret в манифесте развертывания процесса-исполнителя. Внесите изменения в сгенерированный утилитой Kompose файл worker-deployment.yaml, добавив две переменные среды:

• DBPASS — пароль базы данных, который теперь будет извлекаться из объекта Secret fbe-secret;
• DATABASE_URL — полная строка соединения для PostgreSQL, включающая пароль базы данных, на который ссылается в виде ${DBPASS}.

Модифицированная версия файла worker-deployment.yaml выглядит так:

$ cat worker-deployment.yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    kompose.cmd: kompose convert
    kompose.version: 1.16.0 (0c01309)
  creationTimestamp: null
  labels:
    io.kompose.service: worker
  name: worker