---
source_image: page_364.png
page_number: 364
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.79
tokens: 7283
characters: 1237
timestamp: 2025-12-24T03:10:17.148806
finish_reason: stop
---

Создайте объект Service с помощью команды kubectl create -f:

$ kubectl create -f db-service.yaml
service/db created

Выводим список всех сервисов и убеждаемся, что сервис db создан:

$ kubectl get services
NAME      TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
db        ClusterIP      10.110.108.96  <none>        5432/TCP  6s
kubernetes  ClusterIP    10.96.0.1      <none>        443/TCP   4h45m

Следующий сервис, который нам нужно развернуть, — Redis. Создайте объекты Deployment и Service на основе сгенерированных Kompose файлов манифестов:

$ cat redis-deployment.yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    kompose.cmd: kompose convert
    kompose.version: 1.16.0 (0c01309)
  creationTimestamp: null
  labels:
    io.kompose.service: redis
  name: redis
spec:
  replicas: 1
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        io.kompose.service: redis
    spec:
      containers:
      - image: redis:alpine
        name: redis
        ports:
        - containerPort: 6379
          resources: {}
        restartPolicy: Always
status: {}

$ kubectl create -f redis-deployment.yaml
deployment.extensions/redis created

$ kubectl get pods