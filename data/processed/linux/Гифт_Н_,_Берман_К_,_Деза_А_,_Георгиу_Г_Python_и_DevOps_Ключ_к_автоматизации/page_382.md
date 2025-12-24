---
source_image: page_382.png
page_number: 382
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.34
tokens: 7725
characters: 2177
timestamp: 2025-12-24T03:11:09.994573
finish_reason: stop
---

Убеждаемся, что работают три модуля процесса-исполнителя:

$ kubectl get pods
NAME                                 READY   STATUS    RESTARTS   AGE
canary-aqw8jtfo-f54b9749-q5wqj      1/1     Running   0          39m
db-6b4fbb57d9-8h978                  1/1     Running   0          16m
redis-9946db5cc-8g6zz               1/1     Running   0          34m
worker-8cf5dc699-98z99              1/1     Running   0          35s
worker-8cf5dc699-9s26v               1/1     Running   0          35s
worker-8cf5dc699-v6ckr              1/1     Running   0          35s

$ kubectl logs worker-8cf5dc699-98z99
18:28:08 RQ worker 'rq:worker:1355d2cad49646e4953c6b4d978571f1' started,
version 1.0
18:28:08 *** Listening on default...

Аналогично задаем параметр replicas в файле app-deployment.yaml равным 2:

$ kubectl create -f app-deployment.yaml
deployment.extensions/app created

Удостоверяемся, что работают два модуля приложения:

$ kubectl get pods
NAME                                 READY   STATUS    RESTARTS   AGE
app-7964cff98f-5bx4s                 1/1     Running   0          54s
app-7964cff98f-8n8hk                 1/1     Running   0          54s
canary-aqw8jtfo-f54b9749-q5wqj       1/1     Running   0          41m
db-6b4fbb57d9-8h978                  1/1     Running   0          19m
redis-9946db5cc-8g6zz                1/1     Running   0          36m
worker-8cf5dc699-98z99               1/1     Running   0          2m44s
worker-8cf5dc699-9s26v               1/1     Running   0          2m44s
worker-8cf5dc699-v6ckr               1/1     Running   0          2m44s

Создаем сервис app:

$ kubectl create -f app-service.yaml
service/app created

Обратите внимание на то, что был создан сервис типа LoadBalancer:

$ kubectl describe service app
Name:                   app
Namespace:              default
Labels:                 io.kompose.service=app
Annotations:            kompose.cmd: kompose convert
                        kompose.version: 1.16.0 (0c01309)
Selector:              io.kompose.service=app
Type:                   LoadBalancer
IP:                     10.59.255.31
LoadBalancer Ingress:   34.83.242.171
Port:                   5000   5000/TCP