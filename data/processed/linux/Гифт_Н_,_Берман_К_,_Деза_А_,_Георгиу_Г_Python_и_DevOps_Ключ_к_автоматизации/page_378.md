---
source_image: page_378.png
page_number: 378
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.61
tokens: 7458
characters: 1813
timestamp: 2025-12-24T03:10:50.656680
finish_reason: stop
---

Создаем объект PersistentVolumeClaim в качестве тома данных для базы данных PostgreSQL:

$ kubectl create -f dbdata-persistentvolumeclaim.yaml
persistentvolumeclaim/dbdata created

$ kubectl get pvc
NAME      STATUS    VOLUME                CAPACITY
dbdata    Bound     pvc-00c8156c-b618-11e9-9e84-42010a8a006f   1Gi
          ACCESS MODES STORAGECLASS AGE
          RWO           standard    12s

Создаем развертывание db:

$ kubectl create -f db-deployment.yaml
deployment.extensions/db created

$ kubectl get pods
NAME                                 READY   STATUS             RESTARTS   AGE
canary-aqw8jtfo-f54b9749-q5wqj        1/1     Running            0          8m52s
db-6b4fbb57d9-cjjxx                  0/1     CrashLoopBackOff   1          38s
redis-9946db5cc-8g6zz                1/1     Running            0          3m15s

$ kubectl logs db-6b4fbb57d9-cjjxx

initdb: directory "/var/lib/postgresql/data" exists but is not empty
It contains a lost+found directory, perhaps due to it being a mount point.
Using a mount point directly as the data directory is not recommended.
Create a subdirectory under the mount point.

При создании развертывания db мы столкнулись с проблемой. GKE выделил том постоянного хранения, смонтированный на каталог /var/lib/postgresql/data, и, согласно приведенному сообщению об ошибке, непустой.

Удаляем неудачное развертывание db:

$ kubectl delete -f db-deployment.yaml
deployment.extensions "db" deleted

Создаем новый временный модуль для монтирования того же объекта dbdata типа PersistentVolumeClaim в виде каталога /data внутри модуля, чтобы можно было посмотреть на содержимое его файловой системы. Запуск подобного временного модуля для целей отладки — очень полезный прием:

$ cat pvc-inspect.yaml
kind: Pod
apiVersion: v1
metadata:
  name: pvc-inspect
spec: