---
source_image: page_362.png
page_number: 362
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.21
tokens: 7339
characters: 1504
timestamp: 2025-12-24T03:10:17.521074
finish_reason: stop
---

template:
    metadata:
        creationTimestamp: null
        labels:
            io.kompose.service: db
    spec:
        containers:
        - image: postgres:11
          name: postgres
          ports:
          - containerPort: 5432
          resources: {}
          volumeMounts:
          - mountPath: /var/lib/postgresql/data
            name: dbdata
        restartPolicy: Always
        volumes:
        - name: dbdata
          persistentVolumeClaim:
            claimName: dbdata
status: {}

Для создания этого объекта развертывания мы воспользуемся командой kubectl create -f, передав ей имя файла манифеста:

$ kubectl create -f db-deployment.yaml
deployment.extensions/db created

Проверяем, что развертывание было создано, выводя списки всех развертываний в кластере и созданных в качестве части развертывания модулей:

$ kubectl get deployments
NAME     READY   UP-TO-DATE   AVAILABLE   AGE
db       1/1     1           1           1m

$ kubectl get pods
NAME                        READY   STATUS    RESTARTS   AGE
db-67659d85bf-vrnw7         1/1     Running   0          1m

Далее создадим базу данных для нашего примера приложения Flask. С помощью команды, аналогичной docker exec, выполняем команду psql внутри запущенного контейнера Docker. В случае кластера Kubernetes эта команда называется kubectl exec:

$ kubectl exec -it db-67659d85bf-vrnw7 -- psql -U postgres
psql (11.4 (Debian 11.4-1.pgdg90+1))
Type "help" for help.

postgres=# create database wordcount;
CREATE DATABASE