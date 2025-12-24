---
source_image: page_368.png
page_number: 368
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.62
tokens: 7334
characters: 1407
timestamp: 2025-12-24T03:10:32.510989
finish_reason: stop
---

spec:
  replicas: 1
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        io.kompose.service: worker
    spec:
      containers:
      - args:
        - worker.py
      env:
      - name: APP_SETTINGS
        value: config.ProductionConfig
      - name: DBPASS
        valueFrom:
          secretKeyRef:
            name: fbe-secret
            key: dbpass
      - name: DATABASE_URL
        value: postgresql://wordcount_dbadmin:${DBPASS}@db/wordcount
      - name: REDISTOGO_URL
        value: redis://redis:6379
      image: griggheo/flask-by-example:v1
      name: worker
      resources: {}
      restartPolicy: Always
status: {}

Создайте объект Deployment для процесса-исполнителя аналогично прочим развертываниям с помощью команды kubectl create -f:

$ kubectl create -f worker-deployment.yaml
deployment.extensions/worker created

Выводим список модулей:

$ kubectl get pods
NAME                   READY   STATUS    RESTARTS   AGE
db-67659d85bf-vrnw7    1/1     Running   1          21h
redis-c6476fbff-8kpqz  1/1     Running   1          21h
worker-7dbf5ff56c-vgs42 0/1     Init:ErrImagePull   0          7s

Как видите, состояние модуля процесса-исполнителя отображается как Init:Err-ImagePull. Чтобы узнать подробности, выполняем kubectl describe:

$ kubectl describe pod worker-7dbf5ff56c-vgs42 | tail -10
node.kubernetes.io/unreachable:NoExecute for 300s