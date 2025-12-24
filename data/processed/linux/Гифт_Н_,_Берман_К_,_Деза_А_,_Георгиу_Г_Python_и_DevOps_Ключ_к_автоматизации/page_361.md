---
source_image: page_361.png
page_number: 361
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.25
tokens: 7299
characters: 1240
timestamp: 2025-12-24T03:10:12.492716
finish_reason: stop
---

$ cat dbdata-persistentvolumeclaim.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  creationTimestamp: null
  labels:
    io.kompose.service: dbdata
  name: dbdata
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 100Mi
status: {}

Для создания этого объекта в Kubernetes можно воспользоваться командой kubectl create, указав имя файла манифеста с помощью флага -f:

$ kubectl create -f dbdata-persistentvolumeclaim.yaml
persistentvolumeclaim/dbdata created

Выведем полный список всех PVC с помощью команды kubectl get pvc, чтобы убедиться в наличии созданного нами PVC:

$ kubectl get pvc
NAME      STATUS   VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
dbdata    Bound    pvc-39914723-4455-439b-a0f5-82a5f7421475   100Mi
RWO       standard           1m

Следующий шаг — создание объекта Deployment для PostgreSQL. Воспользуемся манифестом db-deployment.yaml, созданным ранее утилитой Kompose:

$ cat db-deployment.yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    kompose.cmd: kompose convert
    kompose.version: 1.16.0 (0c01309)
  creationTimestamp: null
  labels:
    io.kompose.service: db
  name: db
spec:
  replicas: 1
  strategy:
    type: Recreate