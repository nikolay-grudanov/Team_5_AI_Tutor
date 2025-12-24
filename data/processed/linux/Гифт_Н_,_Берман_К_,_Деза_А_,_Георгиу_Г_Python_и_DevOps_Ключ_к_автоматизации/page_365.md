---
source_image: page_365.png
page_number: 365
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.94
tokens: 7527
characters: 1856
timestamp: 2025-12-24T03:10:38.134018
finish_reason: stop
---

NAME                READY   STATUS    RESTARTS   AGE
db-67659d85bf-vrnw7  1/1     Running   0          37m
redis-c6476fbff-8kpqz 1/1     Running   0          11s

$ kubectl create -f redis-service.yaml
service/redis created

$ cat redis-service.yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
    kompose.cmd: kompose convert
    kompose.version: 1.16.0 (0c01309)
  creationTimestamp: null
  labels:
    io.kompose.service: redis
  name: redis
spec:
  ports:
  - name: "6379"
    port: 6379
    targetPort: 6379
  selector:
    io.kompose.service: redis
status:
  loadBalancer: {}

$ kubectl get services
NAME      TYPE           CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
db        ClusterIP      10.110.108.96 <none>       5432/TCP   84s
kubernetes ClusterIP     10.96.0.1    <none>       443/TCP    4h46m
redis     ClusterIP      10.106.44.183 <none>      6379/TCP   10s

Пока что развернутые нами два сервиса, db и redis, друг с другом никак не связаны. Следующая часть приложения — процесс-исполнитель, который должен взаимодействовать как с PostgreSQL, так и с Redis. Здесь и проявляются преимущества сервисов Kubernetes. Развертывание процесса-исполнителя может ссылаться на конечные точки PostgreSQL и Redis по названиям сервисов. Kubernetes будет знать, как перенаправить запросы от клиента (контейнеров, работающих в качестве частей модулей в развертывании процесса-исполнителя) серверам (контейнерам PostgreSQL и Redis, работающим в качестве частей модулей в развертываниях db и redis соответственно).

В число переменных среды в развертывании процесса-исполнителя входит DATABASE_URL. В ней хранится пароль используемой приложением базы данных. Пароль нельзя указывать открытым текстом в файле манифеста развертывания, поскольку этот файл должен вноситься в систему контроля версий. Так что необходимо создать объект Secret Kubernetes.