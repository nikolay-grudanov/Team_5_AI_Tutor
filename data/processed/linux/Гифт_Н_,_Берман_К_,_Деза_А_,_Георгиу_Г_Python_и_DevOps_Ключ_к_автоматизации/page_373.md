---
source_image: page_373.png
page_number: 373
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.84
tokens: 7376
characters: 1377
timestamp: 2025-12-24T03:10:42.529168
finish_reason: stop
---

ports:
    - containerPort: 5000
      resources: {}
      restartPolicy: Always
status: {}

Создаем развертывание для приложения с помощью команды kubectl create -f, после чего выводим список модулей и информацию о модуле приложения:

$ kubectl create -f app-deployment.yaml
deployment.extensions/app created

$ kubectl get pods
NAME                   READY   STATUS    RESTARTS   AGE
app-c845d8969-18nhg    1/1     Running   0          7s
db-67659d85bf-vrnw7     1/1     Running   1          22h
redis-c6476fbff-8kpqz   1/1     Running   1          21h
worker-7dbf5ff56c-vgs42 1/1     Running   0          4m53s

Последний элемент развертывания приложения в minikube — позаботиться о создании сервиса Kubernetes для приложения, причем объявленного с типом LoadBalancer, чтобы к нему можно было обращаться извне кластера:

$ cat app-service.yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
    kompose.cmd: kompose convert
    kompose.version: 1.16.0 (0c01309)
  creationTimestamp: null
  labels:
    io.kompose.service: app
  name: app
spec:
  ports:
  - name: "5000"
    port: 5000
    targetPort: 5000
  type: LoadBalancer
  selector:
    io.kompose.service: app
  status:
    loadBalancer: {}

Как и сервис db, сервис app связывается с развертыванием app через объявление метки, одинаковое в манифестах развертывания и сервиса:

labels:
  io.kompose.service: app